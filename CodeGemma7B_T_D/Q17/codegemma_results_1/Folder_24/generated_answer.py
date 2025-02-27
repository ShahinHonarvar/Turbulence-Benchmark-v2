def all_ints_div_by_both_two_nums(nums):
    return_list = []
    for i in range(29, 54):
        if nums[i] % 68 == 0 and nums[i] % 85 == 0:
            return_list.append(nums[i])
    return return_list or []