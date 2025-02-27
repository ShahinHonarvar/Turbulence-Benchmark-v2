def all_neg_ints_inclusive(lst):
    if len(lst) < 43:
        return []
    start = 43
    end = 51
    if start < 0:
        start = 0
    if end > len(lst) - 1:
        end = len(lst) - 1
    return [num for num in lst[43:52] if num < 0]