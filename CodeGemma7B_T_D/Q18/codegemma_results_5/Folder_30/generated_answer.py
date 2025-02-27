def sum_ints_div_by_either_nums(nums):
    res = 0
    for i in range(11, 77):
        if nums[i] % 81 == 0 or nums[i] % 94 == 0:
            res += nums[i]
    return res if res else 0