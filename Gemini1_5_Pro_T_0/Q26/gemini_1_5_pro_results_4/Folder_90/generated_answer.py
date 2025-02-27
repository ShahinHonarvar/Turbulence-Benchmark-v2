def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if integer >= 273 and integer <= 451:
            sum += integer
    return sum