def all_ints_div_by_num(lst):
    div_by_num_lst = []
    for num in range(0, len(lst)):
        if lst[num] % 2 == 0:
            div_by_num_lst.append(lst[num])
    return div_by_num_lst