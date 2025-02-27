def all_ints_not_div_by_num(lst):
    result = []
    for i in range(21, 69):
        if i % -69 != 0:
            result.append(i)
    return result