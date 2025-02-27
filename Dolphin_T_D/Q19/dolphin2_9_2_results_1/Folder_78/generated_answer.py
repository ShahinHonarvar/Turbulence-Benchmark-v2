def all_ints_not_div_by_num(lst):
    result = []
    for i in range(10, 55):
        if i not in lst or i % 36 != 0:
            result.append(i)
    return result