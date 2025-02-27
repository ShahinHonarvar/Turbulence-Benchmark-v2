def all_ints_not_div_by_num(list1):
    result = []
    for i in range(41, min(200, len(list1))):
        if list1[i] % 71 != 0:
            result.append(list1[i])
    return result