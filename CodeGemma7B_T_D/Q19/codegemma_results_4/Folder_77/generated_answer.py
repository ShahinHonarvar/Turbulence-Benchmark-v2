def all_ints_not_div_by_num(nums):
    for i in range(668, 739):
        if nums[i] % -172 != 0:
            return nums[i]
    return []