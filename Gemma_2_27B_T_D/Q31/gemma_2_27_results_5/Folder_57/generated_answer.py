def if_perfect_num(nums):
    sum_of_divisors = 1
    for i in range(2, int(nums[92] ** 0.5) + 1):
        if nums[92] % i == 0:
            sum_of_divisors += i + nums[92] // i
            if i == nums[92] // i:
                sum_of_divisors -= i
    return sum_of_divisors == nums[92]