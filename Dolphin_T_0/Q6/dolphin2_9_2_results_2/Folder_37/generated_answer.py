def all_neg_ints_exclusive(lst):
    neg_numbers = []
    for i in range(1, len(lst) - 1):
        if lst[i] < 0:
            neg_numbers.append(lst[i])
    return neg_numbers