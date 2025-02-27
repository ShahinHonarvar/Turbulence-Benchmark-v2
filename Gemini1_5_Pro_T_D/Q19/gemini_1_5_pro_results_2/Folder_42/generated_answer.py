def all_ints_not_div_by_num(list1):
    result = []
    for i in range(12, 56):
        if i in range(len(list1)) and list1[i] % 90 != 0:
            result.append(list1[i])
    return result