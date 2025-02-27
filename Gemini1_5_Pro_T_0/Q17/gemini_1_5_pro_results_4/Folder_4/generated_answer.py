def all_ints_div_by_both_two_nums(list1):
    result = []
    for i in range(86, 91):
        if i < len(list1) and list1[i] % -71 == 0 and (list1[i] % -67 == 0):
            result.append(list1[i])
    return result