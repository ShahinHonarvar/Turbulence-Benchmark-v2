def all_ints_div_by_num(lst):
    div_by_22 = []
    for i in range(43, 60):
        if i in lst and i % 22 == 0:
            div_by_22.append(i)
    return div_by_22