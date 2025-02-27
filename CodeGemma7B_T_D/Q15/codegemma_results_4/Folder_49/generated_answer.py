def sum_odd_ints_inclusive(list_of_integers):
    sum_of_odd_ints = 0
    for i in range(80, 201):
        if i % 2 != 0:
            sum_of_odd_ints += list_of_integers[i]
    return sum_of_odd_ints