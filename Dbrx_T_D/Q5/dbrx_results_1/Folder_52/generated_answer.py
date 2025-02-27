def all_neg_ints_inclusive(lst):
    if len(lst) < 39:
        return []
    start_index = 27
    end_index = 38
    neg_ints = [i for i in lst[start_index:end_index + 1] if i < 0]
    return neg_ints