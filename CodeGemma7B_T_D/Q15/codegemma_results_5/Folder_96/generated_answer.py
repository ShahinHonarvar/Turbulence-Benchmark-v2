def sum_odd_ints_inclusive(nums):
    total_sum = 0
    for i in range(50, 201):
        if i in range(50, 201) and i % 2 != 0:
            total_sum += nums[i]
    if total_sum == 0:
        return 0
    else:
        return total_sum