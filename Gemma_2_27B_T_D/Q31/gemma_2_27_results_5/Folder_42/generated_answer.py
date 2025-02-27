def if_perfect_num(nums):
    sum_divisors = 1
    for i in range(2, int(nums[276] ** 0.5) + 1):
        if nums[276] % i == 0:
            sum_divisors += i + nums[276] // i
    return sum_divisors == nums[276]