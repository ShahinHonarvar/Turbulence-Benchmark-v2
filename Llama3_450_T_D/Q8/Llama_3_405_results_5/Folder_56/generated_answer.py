def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if 7 < i < 9 and num % 2 == 0]