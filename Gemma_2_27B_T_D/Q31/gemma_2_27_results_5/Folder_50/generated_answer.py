def if_perfect_num(nums):
    if len(nums) > 40:
        sum_divisors = 1
        for i in range(2, int(nums[40] ** 0.5) + 1):
            if nums[40] % i == 0:
                sum_divisors += i + nums[40] // i
        return sum_divisors == nums[40]
    return False