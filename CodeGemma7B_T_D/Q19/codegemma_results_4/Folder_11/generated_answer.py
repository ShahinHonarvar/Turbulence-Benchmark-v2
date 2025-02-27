def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[36:85]:
        if i % 27 != 0:
            result.append(i)
    return result