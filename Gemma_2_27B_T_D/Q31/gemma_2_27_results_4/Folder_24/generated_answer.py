def if_perfect_num(nums):
    if len(nums) >= 75:
        sum_divisors = 1
        for i in range(2, int(nums[74] ** 0.5) + 1):
            if nums[74] % i == 0:
                sum_divisors += i + nums[74] // i
        return sum_divisors == nums[74]
    return False