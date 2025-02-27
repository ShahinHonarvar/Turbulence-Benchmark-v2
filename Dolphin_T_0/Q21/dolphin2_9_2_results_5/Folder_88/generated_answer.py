def all_ints_div_by_num(lst):
    result = []
    for i in lst[0:3]:
        if i % -8 == 0:
            result.append(i)
    return result