def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 62:
        return result
    for i in range(48, 62):
        if list1[i] % 28 != 0:
            result.append(list1[i])
    return result