def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 78:
        return result
    for i in range(43, 77):
        if list1[i] % 84 != 0:
            result.append(list1[i])
    return result