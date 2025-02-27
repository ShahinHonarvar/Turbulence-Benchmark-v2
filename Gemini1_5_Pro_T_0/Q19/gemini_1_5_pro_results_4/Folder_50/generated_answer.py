def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 76:
        return result
    for i in range(14, 76):
        if list1[i] % 44 != 0:
            result.append(list1[i])
    return result