def all_pos_ints_inclusive(list1):
    positives = []
    for i in range(639, 976):
        if i >= len(list1):
            break
        if list1[i] > 0:
            positives.append(list1[i])
    return positives