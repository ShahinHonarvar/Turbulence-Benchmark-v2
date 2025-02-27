def all_pos_ints_inclusive(list1):
    positive_ints = []
    for i in range(20, 201):
        if i in list1 and list1[i] > 0:
            positive_ints.append(list1[i])
    return positive_ints