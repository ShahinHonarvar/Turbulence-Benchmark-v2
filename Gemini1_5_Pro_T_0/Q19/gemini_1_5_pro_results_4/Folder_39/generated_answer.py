def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 98:
        return result
    for i in range(22, 97):
        if list1[i] % -46 != 0:
            result.append(list1[i])
    return result