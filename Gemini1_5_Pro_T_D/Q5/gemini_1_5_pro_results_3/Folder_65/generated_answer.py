def all_neg_ints_inclusive(list_in):
    neg_ints = []
    for i in range(56, 99):
        if i >= len(list_in):
            break
        if list_in[i] < 0:
            neg_ints.append(list_in[i])
    return neg_ints