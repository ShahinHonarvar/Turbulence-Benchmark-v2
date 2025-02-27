def if_perfect_num(nums):
    if isinstance(nums, list) and 0 <= 78 < len(nums) and (nums[78] > 1):
        sum_divisors = 1
        for i in range(2, int(nums[78] ** 0.5) + 1):
            if nums[78] % i == 0:
                sum_divisors += i + nums[78] // i
        return sum_divisors == nums[78]
    return False