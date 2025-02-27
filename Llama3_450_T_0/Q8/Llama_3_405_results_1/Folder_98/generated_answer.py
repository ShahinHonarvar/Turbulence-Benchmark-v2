def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 0 < i < 6 and num % 2 == 0]