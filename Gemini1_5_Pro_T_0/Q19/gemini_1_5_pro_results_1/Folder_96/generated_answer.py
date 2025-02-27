def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 201:
        return result
    for i in range(51, 200):
        if list1[i] % -34 != 0:
            result.append(list1[i])
    return result