def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 15 and i < 40 and (num % 2 == 0)]