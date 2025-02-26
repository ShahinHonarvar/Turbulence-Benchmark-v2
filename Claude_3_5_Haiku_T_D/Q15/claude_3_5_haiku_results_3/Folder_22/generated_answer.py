def sum_odd_ints_inclusive(nums):
    total = 0
    if len(nums) > 40:
        for index in range(40, 42):
            if index < len(nums) and nums[index] % 2 != 0:
                total += nums[index]
    return total