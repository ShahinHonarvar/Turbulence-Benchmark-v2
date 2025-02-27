def all_ints_not_div_by_num(list1):
    list2 = []
    if len(list1) < 92:
        return list2
    for i in range(46, 91):
        if list1[i] % 67 != 0:
            list2.append(list1[i])
    return list2