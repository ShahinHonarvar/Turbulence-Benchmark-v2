def all_odd_ints_inclusive(lst):
    result = [i for i in lst[22:89] if i % 2 != 0]
    return result if len(result) > 0 else []