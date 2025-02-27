def sum_odd_ints_inclusive(nums):
    total = 0
    for i in range(66, 94):
        if i % 2 != 0:
            total += nums[i]
    if total == 0:
        return 0
    else:
        return total