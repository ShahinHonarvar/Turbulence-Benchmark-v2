def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 6:
        return result
    for i in range(4, 5):
        if list1[i] % -7 != 0:
            result.append(list1[i])
    return result