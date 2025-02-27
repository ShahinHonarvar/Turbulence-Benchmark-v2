def sum_even_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 26 <= i <= 52 and num % 2 == 0))