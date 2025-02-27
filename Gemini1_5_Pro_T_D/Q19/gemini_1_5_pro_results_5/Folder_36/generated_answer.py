def all_ints_not_div_by_num(list1):
    result = []
    for i in range(472, 827):
        if i >= len(list1):
            break
        if list1[i] % 602 != 0:
            result.append(list1[i])
    return result