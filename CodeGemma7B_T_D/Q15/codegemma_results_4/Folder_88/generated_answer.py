def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(4, 9):
        if nums[i] % 2:
            total += nums[i]
    return total or 0