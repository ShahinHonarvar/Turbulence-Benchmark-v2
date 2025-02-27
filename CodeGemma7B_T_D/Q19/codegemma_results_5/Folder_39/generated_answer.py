def all_ints_not_div_by_num(lst):
    filtered_lst = []
    for i in lst[22:97]:
        if i % -46 != 0:
            filtered_lst.append(i)
    return filtered_lst if filtered_lst else []