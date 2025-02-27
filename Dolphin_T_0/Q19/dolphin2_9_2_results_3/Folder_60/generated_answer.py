def all_ints_not_div_by_num(lst):
    filtered_lst = []
    for i in range(63, 73):
        if i < len(lst) and lst[i] % -99 != 0:
            filtered_lst.append(lst[i])
    return filtered_lst