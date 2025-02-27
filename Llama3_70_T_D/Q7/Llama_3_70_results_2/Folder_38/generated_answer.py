def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst[22:64], 22) if num % 2 == 0]