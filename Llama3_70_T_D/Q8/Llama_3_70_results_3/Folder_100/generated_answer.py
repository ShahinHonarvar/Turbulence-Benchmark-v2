def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst[22:25]) if i not in (0, 1, 2) and num % 2 == 0]