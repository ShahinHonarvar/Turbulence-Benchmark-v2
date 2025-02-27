def all_even_ints_inclusive(lst):
    return [x for x in lst[lst[0]:lst[1] + 1] if x % 2 == 0]