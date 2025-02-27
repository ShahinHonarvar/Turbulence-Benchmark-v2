def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[:11]) if num % 2 == 0]