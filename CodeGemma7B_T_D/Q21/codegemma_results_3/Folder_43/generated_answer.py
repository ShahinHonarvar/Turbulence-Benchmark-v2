def all_ints_div_by_num(nums):
    new_list = []
    for i in range(10, 38):
        if nums[i] % -64 == 0:
            new_list.append(nums[i])
    return new_list