def all_odd_ints_inclusive(lst):
    if len(lst) < 33 or not all((isinstance(i, int) for i in lst)):
        return []
    return [i for i in lst[28:33] if i % 2 != 0]