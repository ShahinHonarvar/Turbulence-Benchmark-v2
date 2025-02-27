def all_ints_not_div_by_num(list1):
    result = []
    for i in range(34, 78):
        if i < len(list1) and list1[i] % -17 != 0:
            result.append(list1[i])
    return result