def sum_odd_ints_inclusive(nums):
    total_sum = 0
    for i in range(533, 606):
        if i % 2 != 0:
            total_sum += nums[i]
    if total_sum == 0:
        return 0
    else:
        return total_sum