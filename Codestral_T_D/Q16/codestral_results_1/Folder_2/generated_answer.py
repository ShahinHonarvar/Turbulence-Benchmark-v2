def sum_even_ints_inclusive(list_of_ints):
    return sum((num for num in list_of_ints[15:40] if num % 2 == 0))