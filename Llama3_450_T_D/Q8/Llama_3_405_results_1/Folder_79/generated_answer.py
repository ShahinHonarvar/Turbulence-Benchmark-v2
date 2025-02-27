def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 3 < i < 8 and num % 2 == 0]