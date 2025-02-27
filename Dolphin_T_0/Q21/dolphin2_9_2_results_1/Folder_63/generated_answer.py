def all_ints_div_by_num(lst):
    div_by_num = []
    for i in lst[50:55]:
        if i % 84 == 0:
            div_by_num.append(i)
    return div_by_num