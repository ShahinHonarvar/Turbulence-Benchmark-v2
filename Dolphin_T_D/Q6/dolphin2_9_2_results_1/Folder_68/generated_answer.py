def all_neg_ints_exclusive(lst):
    neg_integers = []
    for i in range(1, len(lst) - 1):
        if lst[i] < 0:
            neg_integers.append(lst[i])
    return neg_integers