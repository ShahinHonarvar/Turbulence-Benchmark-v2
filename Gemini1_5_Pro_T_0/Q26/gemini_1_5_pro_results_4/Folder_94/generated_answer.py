def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if integer >= 36 and integer <= 52:
            sum += integer
    return sum