def all_pos_ints_inclusive(list1):
    list2 = []
    for i in range(32, 36):
        if i >= len(list1):
            break
        if list1[i] > 0:
            list2.append(list1[i])
    return list2