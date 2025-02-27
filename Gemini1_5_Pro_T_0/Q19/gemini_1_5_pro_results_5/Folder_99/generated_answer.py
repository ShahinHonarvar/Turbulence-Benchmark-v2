def all_ints_not_div_by_num(list1):
    list2 = []
    for i in range(388, 516):
        if i >= len(list1):
            break
        if list1[i] % 310 != 0:
            list2.append(list1[i])
    return list2