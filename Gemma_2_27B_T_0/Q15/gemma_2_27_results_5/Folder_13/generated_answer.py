def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(25, 88):
        if nums[i] % 2 != 0:
            total += nums[i]
    return total