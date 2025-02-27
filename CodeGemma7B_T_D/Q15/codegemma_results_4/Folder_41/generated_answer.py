def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(6, min(len(nums), 7) + 1):
        if nums[i] % 2 != 0:
            total += nums[i]
    return total