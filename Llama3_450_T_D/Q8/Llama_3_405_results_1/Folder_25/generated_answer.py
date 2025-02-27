def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 41 and i < 69 and (num % 2 == 0)]