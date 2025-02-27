def all_ints_div_by_num(list1):
    result = []
    for i in range(23, 66):
        if i < len(list1) and list1[i] % -46 == 0:
            result.append(list1[i])
    return result