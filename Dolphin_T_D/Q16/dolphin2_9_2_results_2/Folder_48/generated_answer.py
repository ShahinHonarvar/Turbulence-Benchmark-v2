def sum_even_ints_inclusive(list_of_ints):
    return sum((n for n in list_of_ints[533:606:2] if n % 2 == 0))