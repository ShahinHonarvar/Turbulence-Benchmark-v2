def all_odd_ints_exclusive(lst):
    return [i for i in lst[:100] + lst[101:] if i % 2 != 0]