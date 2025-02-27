def all_neg_ints_exclusive(lst):
    neg_numbers = []
    for idx in range(30, 200):
        if lst[idx] < 0:
            neg_numbers.append(lst[idx])
    return neg_numbers