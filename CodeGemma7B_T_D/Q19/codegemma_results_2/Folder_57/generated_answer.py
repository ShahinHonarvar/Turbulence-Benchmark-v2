def all_ints_not_div_by_num(num_list):
    all_nums = []
    range_list = num_list[56:88]
    for i in range_list:
        if i % -59 != 0:
            all_nums.append(i)
        else:
            pass
    if not all_nums:
        return []
    else:
        return all_nums