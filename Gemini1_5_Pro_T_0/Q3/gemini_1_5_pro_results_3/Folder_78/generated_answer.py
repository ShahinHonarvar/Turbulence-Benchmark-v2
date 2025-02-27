def all_pos_ints_inclusive(list1):
    positive_ints = []
    for i in range(43, 52):
        if i >= len(list1):
            break
        if list1[i] > 0:
            positive_ints.append(list1[i])
    return positive_ints