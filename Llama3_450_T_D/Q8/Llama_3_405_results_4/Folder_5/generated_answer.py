def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 2 < i < 7 and num % 2 == 0]