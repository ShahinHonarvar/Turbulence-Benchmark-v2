def all_neg_ints_inclusive(list_of_integers):
    neg_ints = []
    for i in range(533, 606):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] < 0:
            neg_ints.append(list_of_integers[i])
    return neg_ints