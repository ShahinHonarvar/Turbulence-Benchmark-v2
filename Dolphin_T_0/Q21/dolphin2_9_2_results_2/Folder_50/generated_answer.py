def all_ints_div_by_num(lst):
    div_by_28 = []
    for i in range(36, 47):
        if lst[i] % 28 == 0:
            div_by_28.append(lst[i])
    return div_by_28