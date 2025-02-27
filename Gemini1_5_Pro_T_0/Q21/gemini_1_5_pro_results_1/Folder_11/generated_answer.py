def all_ints_div_by_num(list1):
    result = []
    for i in range(22, 64):
        if i < len(list1) and list1[i] % -61 == 0:
            result.append(list1[i])
    return result