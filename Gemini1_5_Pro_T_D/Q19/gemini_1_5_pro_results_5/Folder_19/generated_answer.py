def all_ints_not_div_by_num(list1):
    result = []
    for i in range(max(4, len(list1) - 1)):
        if i > 4:
            if list1[i] % -7 != 0:
                result.append(list1[i])
    return result