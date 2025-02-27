def all_ints_not_div_by_num(lst):
    result = []
    for i in range(19, 49):
        if i % -36 != 0:
            result.append(lst[i])
    return result