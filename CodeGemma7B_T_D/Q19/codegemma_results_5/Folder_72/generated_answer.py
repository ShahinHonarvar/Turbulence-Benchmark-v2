def all_ints_not_div_by_num(nums):
    new_list = []
    for i in range(13, 70):
        if nums[i] % -78 != 0:
            new_list.append(nums[i])
    return new_list