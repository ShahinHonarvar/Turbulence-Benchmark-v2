def all_neg_ints_inclusive(lst):
    return [lst[i] for i in range(min(6, len(lst))) if lst[i] < 0]