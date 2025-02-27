def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) >= 71:
        for i in range(43, 70):
            if list1[i] % 69 != 0:
                result.append(list1[i])
    return result