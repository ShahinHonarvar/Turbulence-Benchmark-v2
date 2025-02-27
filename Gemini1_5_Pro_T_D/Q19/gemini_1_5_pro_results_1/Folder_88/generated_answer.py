def all_ints_not_div_by_num(list1):
    result = []
    for i in range(max(4, 0), min(len(list1), 7)):
        if list1[i] % -6 != 0:
            result.append(list1[i])
    return result