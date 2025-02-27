def if_perfect_num(nums):
    sum_of_divisors = 1
    for i in range(2, int(nums[91] ** 0.5) + 1):
        if nums[91] % i == 0:
            sum_of_divisors += i + nums[91] // i
    return sum_of_divisors == nums[91]