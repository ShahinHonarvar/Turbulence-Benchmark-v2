def sum_ints_div_by_either_nums(nums):
    k = 0
    for i in range(1, 5):
        if nums[i] % 4 == 0 or nums[i] % -6 == 0:
            k += nums[i]
    if k == 0:
        return 0
    else:
        return k