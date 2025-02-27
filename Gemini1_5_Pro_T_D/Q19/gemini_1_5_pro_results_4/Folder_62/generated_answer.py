def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 93:
        return result
    for i in range(15, 92):
        if list1[i] % 59 != 0:
            result.append(list1[i])
    return result