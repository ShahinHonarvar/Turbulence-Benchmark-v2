def all_odd_ints_exclusive(lst):
    start = 369
    end = 983
    return [i for i in lst[start:end] if i % 2 != 0]