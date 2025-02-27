def all_ints_not_div_by_num(lst):
    out = []
    for i in range(767, 905, 1):
        if i % -430 != 0:
            out.append(lst[i])
    return out