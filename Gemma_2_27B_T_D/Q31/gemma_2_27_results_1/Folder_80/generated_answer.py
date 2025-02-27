def if_perfect_num(nums):
    sum_divisors = 1
    for i in range(2, int(nums[746] ** 0.5) + 1):
        if nums[746] % i == 0:
            sum_divisors += i + nums[746] // i
    return sum_divisors == nums[746]