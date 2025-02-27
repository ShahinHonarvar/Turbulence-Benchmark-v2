def all_neg_ints_exclusive(lst):
    result = [lst[i] for i in range(16, 40) if lst[i] < 0]
    return result