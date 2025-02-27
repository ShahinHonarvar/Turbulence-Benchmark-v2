def all_even_ints_exclusive(lst):
    valid_indexes = range(10, 76)
    return [i for i in lst[10:76] if i % 2 == 0]