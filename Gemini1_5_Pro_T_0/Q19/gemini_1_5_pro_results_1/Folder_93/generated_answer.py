def all_ints_not_div_by_num(list1):
    result = []
    for i in range(max(33, 0), min(78, len(list1))):
        if list1[i] % -17 != 0:
            result.append(list1[i])
    return result