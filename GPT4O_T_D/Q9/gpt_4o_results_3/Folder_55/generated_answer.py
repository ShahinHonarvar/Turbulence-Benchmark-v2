def all_odd_ints_inclusive(lst):
    if len(lst) > 10 and lst[10] % 2 != 0:
        return [lst[10]]
    return []