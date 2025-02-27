def sum_even_ints_inclusive(lst):
    return sum((num for idx, num in enumerate(lst) if 13 <= idx <= 68 and num % 2 == 0))