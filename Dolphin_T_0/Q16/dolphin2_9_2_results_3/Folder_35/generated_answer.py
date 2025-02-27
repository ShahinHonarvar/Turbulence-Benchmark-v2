def sum_even_ints_inclusive(list_of_ints):
    return sum((int for i, int in enumerate(list_of_ints[30:49]) if int % 2 == 0))