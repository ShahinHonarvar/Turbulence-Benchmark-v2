def all_ints_not_div_by_num(list1):
    result = []
    for i in range(39, 81):
        if i < len(list1) and list1[i] % 49 != 0:
            result.append(list1[i])
    return result