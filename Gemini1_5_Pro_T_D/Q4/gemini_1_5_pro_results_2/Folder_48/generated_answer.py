def all_pos_ints_exclusive(list1):
    positives = []
    for i in range(386, 999):
        if i < len(list1) and list1[i] > 0:
            positives.append(list1[i])
    return positives