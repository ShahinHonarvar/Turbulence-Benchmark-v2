def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(74, 96):
        if i % 2 == 1:
            sum_odd += nums[i]
    if sum_odd == 0:
        return 0
    else:
        return sum_odd