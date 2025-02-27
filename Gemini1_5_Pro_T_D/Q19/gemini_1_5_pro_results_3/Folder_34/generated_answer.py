def all_ints_not_div_by_num(list1):
    result = []
    if len(list1) >= 200:
        for i in range(61, 200):
            if list1[i] % 9 != 0:
                result.append(list1[i])
        return result
    else:
        return result