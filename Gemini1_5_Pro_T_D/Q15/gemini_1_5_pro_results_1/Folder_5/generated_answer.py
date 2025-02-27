def sum_odd_ints_inclusive(list_of_integers):
    sum = 0
    for i in range(8, 10):
        if i >= len(list_of_integers):
            break
        if list_of_integers[i] % 2 != 0:
            sum += list_of_integers[i]
    return sum