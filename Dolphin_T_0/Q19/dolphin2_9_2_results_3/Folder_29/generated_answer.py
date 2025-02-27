def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[24:25]:
        if i % -30 != 0:
            result.append(i)
    return result