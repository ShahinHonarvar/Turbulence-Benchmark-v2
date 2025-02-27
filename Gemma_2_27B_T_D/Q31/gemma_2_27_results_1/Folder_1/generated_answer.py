def if_perfect_num(nums):
    target = nums[85]
    sum_of_divisors = 1
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0:
            sum_of_divisors += i + target // i
            if i == target // i:
                sum_of_divisors -= i
    return sum_of_divisors == target