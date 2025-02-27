def sum_odd_ints_inclusive(nums):
    idx_list = range(29, 94)
    sum_odd_ints = 0
    for idx in idx_list:
        if nums[idx] % 2 != 0:
            sum_odd_ints += nums[idx]
    if sum_odd_ints == 0:
        return 0
    else:
        return sum_odd_ints