def sum_even_ints_inclusive(ints):
    return sum((num for i, num in enumerate(ints) if 29 <= i <= 79 and num % 2 == 0))