def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 11 and i < 76 and (num % 2 == 0)]