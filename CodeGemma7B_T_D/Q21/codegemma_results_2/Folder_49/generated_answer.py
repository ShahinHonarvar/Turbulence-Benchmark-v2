def all_ints_div_by_num(lst):
    full_list = []
    for i in range(30, 301):
        if i % 5 == 0 and i in lst:
            full_list.append(i)
    if full_list == []:
        return []
    else:
        return full_list