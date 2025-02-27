def all_ints_not_div_by_num(int_list):
    filtered_list = []
    for i in int_list[767:938]:
        if i % 593 != 0:
            filtered_list.append(i)
    return filtered_list