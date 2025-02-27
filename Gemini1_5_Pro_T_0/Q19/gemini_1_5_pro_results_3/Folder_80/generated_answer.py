def all_ints_not_div_by_num(list1):
    result = []
    for i in range(16, 20):
        if i in range(len(list1)):
            if list1[i] % 93 != 0:
                result.append(list1[i])
    return result