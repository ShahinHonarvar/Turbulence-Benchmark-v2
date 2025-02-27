def all_ints_div_by_num(list1):
    result = []
    for i in range(max(18, len(list1)) - min(len(list1), 93 + 1)):
        if list1[i] % -85 == 0:
            result.append(list1[i])
    return result