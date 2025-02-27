def all_ints_not_div_by_num(list1):
    result = []
    for i in range(64, 80):
        if i >= len(list1) or i < 0:
            break
        if list1[i] % -95 != 0:
            result.append(list1[i])
    return result