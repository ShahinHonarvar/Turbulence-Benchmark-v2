def all_ints_div_by_num(lst):
    div_by_71 = []
    for i in range(13, 69):
        if lst[i] % 71 == 0:
            div_by_71.append(lst[i])
    return div_by_71