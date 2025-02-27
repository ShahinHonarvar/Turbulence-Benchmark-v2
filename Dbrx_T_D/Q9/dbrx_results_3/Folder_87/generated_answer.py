def all_odd_ints_inclusive(lst):
    if len(lst) < 46:
        return []
    result = [i for i in lst[36:47] if i % 2 != 0]
    return result