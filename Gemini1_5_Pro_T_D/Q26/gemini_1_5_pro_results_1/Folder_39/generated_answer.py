def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if integer >= 10 and integer <= 79:
            sum += integer
    return sum