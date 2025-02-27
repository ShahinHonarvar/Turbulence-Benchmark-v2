def all_odd_ints_exclusive(lst):
    return [i for i in lst[101:-1] + lst[:100] if i % 2 != 0]