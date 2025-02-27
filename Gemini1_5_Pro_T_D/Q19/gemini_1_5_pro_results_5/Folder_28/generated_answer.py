def all_ints_not_div_by_num(list1):
    list2 = []
    for i in range(82, 86):
        if i < len(list1) and list1[i] % 77 != 0:
            list2.append(list1[i])
    return list2