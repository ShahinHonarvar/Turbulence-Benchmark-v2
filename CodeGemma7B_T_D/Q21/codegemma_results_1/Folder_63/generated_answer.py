def all_ints_div_by_num(nums):
    int_list = []
    for i in range(50, 55):
        if nums[i] % 84 == 0:
            int_list.append(nums[i])
    return int_list