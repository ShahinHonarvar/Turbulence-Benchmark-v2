def all_odd_ints_inclusive(lst):
    if not 91 <= len(lst) <= 99:
        return []
    return [i for i in lst[91:100] if i % 2 != 0]