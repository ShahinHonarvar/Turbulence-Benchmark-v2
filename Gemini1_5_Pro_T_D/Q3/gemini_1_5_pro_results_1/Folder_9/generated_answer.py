def all_pos_ints_inclusive(list1):
    list2 = []
    for i in range(70, 201):
        if i >= 0 and i < len(list1) and (list1[i] > 0):
            list2.append(list1[i])
    return list2