def all_ints_not_div_by_num(lst):
    result = []
    for x in lst[1:2]:
        if x % 5 != 0:
            result.append(x)
    return result