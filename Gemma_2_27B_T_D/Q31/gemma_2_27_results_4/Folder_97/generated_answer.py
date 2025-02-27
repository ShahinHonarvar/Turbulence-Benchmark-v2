def if_perfect_num(nums):
    if len(nums) <= 132:
        return False
    sum_divisors = 1
    for i in range(2, int(nums[132] ** 0.5) + 1):
        if nums[132] % i == 0:
            sum_divisors += i + nums[132] // i
    return sum_divisors == nums[132]