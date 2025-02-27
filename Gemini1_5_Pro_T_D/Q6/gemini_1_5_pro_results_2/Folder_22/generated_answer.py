def all_neg_ints_exclusive(list1):
    list2 = []
    for i in range(41, 200):
        if i < len(list1) and list1[i] < 0:
            list2.append(list1[i])
    return list2