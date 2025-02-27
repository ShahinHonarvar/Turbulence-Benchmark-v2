def sum_odd_ints_inclusive(list_of_integers):
    sum = 0
    for i in range(min(len(list_of_integers), 10)):
        if list_of_integers[i] % 2 != 0:
            sum += list_of_integers[i]
    return sum