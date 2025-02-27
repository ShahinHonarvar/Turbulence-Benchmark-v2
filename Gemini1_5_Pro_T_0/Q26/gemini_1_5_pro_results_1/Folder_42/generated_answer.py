def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if integer >= 141 and integer <= 262:
            sum += integer
    return sum