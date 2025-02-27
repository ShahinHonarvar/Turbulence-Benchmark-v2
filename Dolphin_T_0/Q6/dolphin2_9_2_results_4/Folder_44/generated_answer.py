def all_neg_ints_exclusive(lst):
    negatives = [num for num in lst[81:86] if num < 0]
    if not negatives:
        return []
    return negatives