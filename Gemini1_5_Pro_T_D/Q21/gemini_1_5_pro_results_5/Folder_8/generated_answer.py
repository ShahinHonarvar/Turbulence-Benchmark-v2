def all_ints_div_by_num(list1):
    result = []
    for i in range(34, 56):
        if i >= len(list1):
            break
        if list1[i] % -83 == 0:
            result.append(list1[i])
    return result