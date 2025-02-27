def sum_even_ints_inclusive(lst):
    return sum((num for idx, num in enumerate(lst) if 209 <= idx <= 556 and num % 2 == 0))