def all_odd_ints_inclusive(lst):
    try:
        return [i for i in lst[28:33] if i % 2 != 0]
    except IndexError:
        return []