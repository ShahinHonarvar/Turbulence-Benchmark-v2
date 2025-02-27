def sum_even_ints_inclusive(list_of_ints):
    return sum((val for i, val in enumerate(list_of_ints[70:201]) if val % 2 == 0))