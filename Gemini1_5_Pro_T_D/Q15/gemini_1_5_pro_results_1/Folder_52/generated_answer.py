def sum_odd_ints_inclusive(list_of_integers):
    sum_of_odd_integers = 0
    for i in range(28, 39):
        if i < len(list_of_integers) and list_of_integers[i] % 2 != 0:
            sum_of_odd_integers += list_of_integers[i]
    return sum_of_odd_integers