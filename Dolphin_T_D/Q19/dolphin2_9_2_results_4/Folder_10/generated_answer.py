def all_ints_not_div_by_num(lst):
    result = []
    for i in range(86, 89):
        if i % -61 != 0:
            result.append(lst[i])
    return result