def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if 136 <= integer <= 618:
            sum += integer
    return sum