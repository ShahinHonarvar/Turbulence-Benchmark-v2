def all_ints_not_div_by_num(list1):
    result = []
    for i in range(45, 91):
        if i < len(list1) and list1[i] % -68 != 0:
            result.append(list1[i])
    return result