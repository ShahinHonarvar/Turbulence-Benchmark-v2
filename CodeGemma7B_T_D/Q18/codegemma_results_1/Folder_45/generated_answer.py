def sum_ints_div_by_either_nums(nums):
    Sum = 0
    for i in range(30, 201):
        if nums[i] % -115 == 0 or nums[i] % 115 == 0:
            Sum += nums[i]
    if not bool(Sum):
        Sum = 0
    return Sum