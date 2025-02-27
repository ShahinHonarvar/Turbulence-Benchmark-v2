def all_ints_not_div_by_num(list1):
    result = []
    for i in range(35, 98):
        if i >= len(list1):
            break
        if list1[i] % 41 != 0:
            result.append(list1[i])
    return result