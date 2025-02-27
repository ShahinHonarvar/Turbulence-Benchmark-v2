def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 91:
        return result
    for i in range(46, 91):
        if list1[i] % 67 != 0:
            result.append(list1[i])
    return result