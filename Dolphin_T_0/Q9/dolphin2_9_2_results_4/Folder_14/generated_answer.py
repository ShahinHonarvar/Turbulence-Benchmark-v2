def all_odd_ints_inclusive(lst):
    result = [x for x in lst[5:8] if x % 2 != 0]
    return result if len(result) > 0 else []