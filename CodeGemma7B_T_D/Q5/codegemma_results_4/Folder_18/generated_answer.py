def all_neg_ints_inclusive(lst):
    for i in range(35, 50):
        if lst[i] < 0:
            return lst[i:i + 2].copy()
    return []