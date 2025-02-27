def all_even_ints_inclusive(lst):
    return [num for idx, num in enumerate(lst) if idx >= 10 and idx <= 100 and (num % 2 == 0)]