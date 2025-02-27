def all_ints_div_by_num(lst):
    result = []
    for x in lst[18:39]:
        if x % -97 == 0:
            result.append(x)
    return result