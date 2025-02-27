def all_neg_ints_exclusive(lst):
    return [neg for neg in lst[386:999] if neg < 0 and 385 < lst.index(neg) < 999]