def sum_even_ints_inclusive(lst):
    return sum((num for i, num in enumerate(lst) if 262 <= i <= 746 and num % 2 == 0))