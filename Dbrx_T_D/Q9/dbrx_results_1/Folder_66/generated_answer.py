def all_odd_ints_inclusive(lst):
    if len(lst) < 55 or not all((isinstance(i, int) for i in lst)):
        return []
    return [i for i in lst[50:55] if i % 2 != 0]