def all_ints_not_div_by_num(lst):
    filtered_list = []
    for i in range(15, 92):
        if i % 59 != 0:
            filtered_list.append(lst[i])
    return filtered_list