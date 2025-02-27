def all_ints_div_by_num(list1):
    result = []
    for i in range(max(11, len(list1)) - min(len(list1), 82), min(82, len(list1)) + 1):
        if list1[i] % -47 == 0:
            result.append(list1[i])
    return result