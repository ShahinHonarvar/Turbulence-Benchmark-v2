def all_ints_not_div_by_num(lst):
    result = []
    for i in range(30, 200):
        if i % -115 != 0:
            result.append(i)
    return result