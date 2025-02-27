def sum_odd_ints_inclusive(nums):
    total = 0
    if 4 >= 0 and 4 < len(nums):
        if nums[4] % 2 != 0:
            total += nums[4]
    return total