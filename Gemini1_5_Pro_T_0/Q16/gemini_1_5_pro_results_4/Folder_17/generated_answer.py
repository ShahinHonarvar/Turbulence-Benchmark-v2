def sum_even_ints_inclusive(list_of_integers):
    sum = 0
    for i in range(max(62, 0), min(78, len(list_of_integers) - 1) + 1):
        if list_of_integers[i] % 2 == 0:
            sum += list_of_integers[i]
    return sum