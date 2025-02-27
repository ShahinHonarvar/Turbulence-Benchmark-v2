def sum_even_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 30 <= i <= 48 and num % 2 == 0))