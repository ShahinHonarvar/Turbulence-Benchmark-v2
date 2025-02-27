def if_perfect_num(nums):
    sum_divisors = 1
    for i in range(2, int(nums[29] ** 0.5) + 1):
        if nums[29] % i == 0:
            sum_divisors += i + nums[29] // i
    return sum_divisors == nums[29]