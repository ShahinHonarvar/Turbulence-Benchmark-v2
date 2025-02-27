def if_perfect_num(nums):
    if len(nums) <= 74:
        return False
    num = nums[74]
    if num <= 1:
        return False
    sum_of_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num