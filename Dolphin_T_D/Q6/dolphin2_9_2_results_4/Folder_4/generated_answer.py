def all_neg_ints_exclusive(lst):
    result = [num for num in lst[11:76] if num < 0]
    return result if result else []