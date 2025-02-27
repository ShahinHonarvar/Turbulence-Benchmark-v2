def all_ints_div_by_both_two_nums(nums):
    lst = []
    for i in range(18, 52):
        if nums[i] % 15 == 0 and nums[i] % 57 == 0:
            lst.append(nums[i])
    return lst if lst else []