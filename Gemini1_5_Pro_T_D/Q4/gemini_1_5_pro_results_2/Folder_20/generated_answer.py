def all_pos_ints_exclusive(ints):
    positives = []
    for i in range(max(0, 60), min(len(ints), 93)):
        if ints[i] > 0:
            positives.append(ints[i])
    return positives