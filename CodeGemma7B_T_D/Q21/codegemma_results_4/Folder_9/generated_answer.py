def all_ints_div_by_num(lst):
    div_num = []
    for i in lst[20:200]:
        if i % 4 == 0:
            div_num.append(i)
    return div_num