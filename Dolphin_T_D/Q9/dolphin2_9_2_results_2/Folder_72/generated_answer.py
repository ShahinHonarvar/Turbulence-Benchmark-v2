def all_odd_ints_inclusive(lst):
    result = [i for i in lst[29:52] if i % 2 != 0]
    return result if len(result) > 0 else []