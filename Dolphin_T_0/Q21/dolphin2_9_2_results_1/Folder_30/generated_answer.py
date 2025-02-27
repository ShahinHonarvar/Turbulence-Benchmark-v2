def all_ints_div_by_num(lst):
    div_by_num = []
    for i in range(59, 80):
        if lst[i] % -82 == 0:
            div_by_num.append(lst[i])
    return div_by_num