def sum_odd_ints_inclusive(list_of_integers):
    sum = 0
    for i in range(209, 557):
        if list_of_integers[i] % 2 != 0:
            sum += list_of_integers[i]
    if sum == 0:
        return 0
    else:
        return sum