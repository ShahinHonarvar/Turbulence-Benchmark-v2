def sum_even_ints_inclusive(list_of_ints):
    return sum((num for num in list_of_ints[22:64] if num % 2 == 0))