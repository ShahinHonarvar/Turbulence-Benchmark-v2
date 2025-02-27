def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 44:
        return result
    for i in range(33, 44):
        if list1[i] % 34 != 0:
            result.append(list1[i])
    return result