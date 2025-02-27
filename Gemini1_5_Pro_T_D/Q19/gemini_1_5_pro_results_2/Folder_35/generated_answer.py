def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) < 58:
        return result
    else:
        for i in range(16, 57):
            if list1[i] % 86 != 0:
                result.append(list1[i])
        return result