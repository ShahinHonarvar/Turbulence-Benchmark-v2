def all_even_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i >= 30 and i <= 200 and (num % 2 == 0)]