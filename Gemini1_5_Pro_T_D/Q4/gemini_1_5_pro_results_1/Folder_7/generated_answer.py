def all_pos_ints_exclusive(l):
    positive_integers = []
    for i in range(323, 972):
        if i < len(l) and l[i] > 0:
            positive_integers.append(l[i])
    return positive_integers