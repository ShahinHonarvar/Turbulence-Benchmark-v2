def all_ints_div_by_num(lst):
    result = []
    for i in lst[42:90]:
        if i % -59 == 0:
            result.append(i)
    return result