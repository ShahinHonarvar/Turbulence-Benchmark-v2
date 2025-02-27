def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 92:
        return result
    for i in range(44, 91):
        if list1[i] % -68 != 0:
            result.append(list1[i])
    return result