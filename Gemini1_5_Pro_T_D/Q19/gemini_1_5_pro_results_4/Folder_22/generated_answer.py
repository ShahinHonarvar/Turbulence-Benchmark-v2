def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 201 or 40 > len(list1):
        return result
    for i in range(40, 200):
        if i < len(list1) and list1[i] % 71 != 0:
            result.append(list1[i])
    return result