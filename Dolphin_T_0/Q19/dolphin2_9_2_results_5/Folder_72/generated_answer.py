def all_ints_not_div_by_num(lst):
    result = []
    for i in range(13, 70):
        if i not in lst:
            if i % -78 != 0:
                result.append(i)
    return result