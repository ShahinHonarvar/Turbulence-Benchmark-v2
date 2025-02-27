def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if integer >= 20 and integer <= 93:
            sum += integer
    return sum