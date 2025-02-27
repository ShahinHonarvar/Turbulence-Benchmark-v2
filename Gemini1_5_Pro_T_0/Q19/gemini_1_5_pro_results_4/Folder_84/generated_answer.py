def all_ints_not_div_by_num(list1):
    list2 = []
    for i in range(50, 81):
        if i in range(len(list1)):
            if list1[i] % 64 != 0:
                list2.append(list1[i])
    return list2