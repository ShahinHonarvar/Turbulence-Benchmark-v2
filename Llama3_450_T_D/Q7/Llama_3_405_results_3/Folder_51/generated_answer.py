def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if 1 <= i <= 8 and num % 2 == 0]