def all_ints_not_div_by_num(list1):
    result = []
    for i in range(31, 200):
        if i < len(list1) and list1[i] % -115 != 0:
            result.append(list1[i])
    return result