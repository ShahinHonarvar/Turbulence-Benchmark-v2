def sum_odd_ints_inclusive(list_of_integers):
    return sum((list_of_integers[i] for i in range(75, 89) if list_of_integers[i] % 2 != 0))