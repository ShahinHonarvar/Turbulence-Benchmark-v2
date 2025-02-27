def all_ints_not_div_by_num(list1):
    result = []
    for i in range(max(63, 0), min(73, len(list1))):
        if list1[i] % -99 != 0:
            result.append(list1[i])
    return result