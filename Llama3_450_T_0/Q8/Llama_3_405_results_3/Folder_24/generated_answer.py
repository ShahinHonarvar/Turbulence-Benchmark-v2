def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 13 < i < 66 and num % 2 == 0]