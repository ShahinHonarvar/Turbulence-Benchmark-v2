def all_ints_not_div_by_num(list1):
    list2 = []
    for j in range(15, 20):
        if list1[j] % 93 != 0:
            list2.append(list1[j])
    if list2 == []:
        return []
    return list2