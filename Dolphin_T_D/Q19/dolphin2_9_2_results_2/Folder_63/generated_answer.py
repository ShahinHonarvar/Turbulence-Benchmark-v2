def all_ints_not_div_by_num(lst):
    result = []
    for i in lst[20:43]:
        if i % 95 != 0:
            result.append(i)
    return result