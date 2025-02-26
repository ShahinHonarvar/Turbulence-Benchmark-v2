def sum_odd_ints_inclusive(nums):
    total = 0
    for index in range(33, 37):
        if 0 <= index < len(nums) and nums[index] % 2 != 0:
            total += nums[index]
    return total