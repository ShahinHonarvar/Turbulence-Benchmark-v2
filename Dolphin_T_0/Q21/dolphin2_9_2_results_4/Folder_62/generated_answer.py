def all_ints_div_by_num(lst):
    div_by_55 = []
    for i in range(87, 90):
        if lst[i] % 55 == 0:
            div_by_55.append(lst[i])
    return div_by_55