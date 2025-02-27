def all_odd_ints_inclusive(lst):
    if len(lst) < 79:
        return []
    return [x for x in lst[17:79] if x % 2 == 1]