def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 13 < i < 76 and num % 2 == 0]