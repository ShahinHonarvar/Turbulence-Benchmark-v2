def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 44 and i < 91 and (num % 2 == 0)]