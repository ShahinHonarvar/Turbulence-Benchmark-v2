def sum_even_ints_inclusive(ints):
    return sum((num for num in ints[:10] if num % 2 == 0))