def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(31, 35):
        if nums[i] % 2 == 1:
            total += nums[i]
    return total