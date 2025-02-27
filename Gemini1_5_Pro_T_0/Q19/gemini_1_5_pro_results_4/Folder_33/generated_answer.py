def all_ints_not_div_by_num(list1):
    result = []
    for i in range(max(103, 0), min(574, len(list1))):
        if list1[i] % -514 != 0:
            result.append(list1[i])
    return result