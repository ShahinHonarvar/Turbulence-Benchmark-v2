def all_pos_ints_inclusive(list1):
    positives = []
    for i in range(max(82, 0), min(len(list1), 87)):
        if list1[i] > 0:
            positives.append(list1[i])
    return positives