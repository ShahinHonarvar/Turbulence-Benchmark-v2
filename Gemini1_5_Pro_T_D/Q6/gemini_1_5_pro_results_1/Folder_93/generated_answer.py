def all_neg_ints_exclusive(list1):
    list2 = []
    for i in range(19, 94):
        if i >= len(list1) or i < 0:
            break
        if list1[i] < 0:
            list2.append(list1[i])
    return list2