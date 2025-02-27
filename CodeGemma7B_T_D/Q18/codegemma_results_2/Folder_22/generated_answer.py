def sum_ints_div_by_either_nums(nums):
    res = 0
    for i in range(40, 201):
        tmp = nums[i]
        if tmp % 21 == 0 or tmp % 71 == 0:
            res += tmp
    return res or 0