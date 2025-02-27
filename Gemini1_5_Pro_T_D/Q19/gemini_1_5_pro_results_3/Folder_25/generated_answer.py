def all_ints_not_div_by_num(list1):
    result = []
    for i in range(max(29, 0), min(53, len(list1))):
        if list1[i] % -68 != 0:
            result.append(list1[i])
    return result