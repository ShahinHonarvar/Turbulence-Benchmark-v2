def sum_odd_ints_inclusive(list_of_integers):
    if not any((num % 2 != 0 for num in list_of_integers[30:88])):
        return 0
    return sum((num for num in list_of_integers[30:88] if num % 2 != 0))