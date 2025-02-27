def sum_odd_ints_inclusive(nums):
    total = 0
    if 6 >= len(nums):
        return total
    if nums[6] % 2 != 0:
        total += nums[6]
    return total