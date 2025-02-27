def sum_odd_ints_inclusive(list_of_integers):
    return sum((value for index, value in enumerate(list_of_integers[70:85]) if index % 2 != 0))