def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[743:867]) if i % 2 == 1]