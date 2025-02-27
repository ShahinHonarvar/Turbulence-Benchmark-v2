def all_ints_div_by_num(list_nums):
    new_list = []
    for i in list_nums[40:400]:
        if i % 7 == 0:
            new_list.append(i)
    return new_list