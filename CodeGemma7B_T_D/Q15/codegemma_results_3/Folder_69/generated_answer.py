def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(32, 36):
        if i >= 0 and i < len(nums):
            if nums[i] % 2 != 0:
                total += nums[i]
    return total