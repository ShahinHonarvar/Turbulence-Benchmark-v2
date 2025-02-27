def all_pos_ints_exclusive(ints):
    positives = []
    for i in range(598, 767):
        if i >= len(ints):
            break
        if ints[i] > 0:
            positives.append(ints[i])
    return positives