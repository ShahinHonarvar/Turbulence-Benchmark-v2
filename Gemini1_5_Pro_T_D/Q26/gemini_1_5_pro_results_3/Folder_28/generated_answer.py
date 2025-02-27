def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if 10 <= integer <= 97:
            sum += integer
    return sum