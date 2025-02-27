def all_ints_not_div_by_num(lst):
    result = []
    for i in range(1, 6):
        if i not in lst or i % 2 != 0:
            result.append(i)
    return result