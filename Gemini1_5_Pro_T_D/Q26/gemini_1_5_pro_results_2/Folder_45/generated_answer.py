def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if integer >= 3 and integer <= 4:
            sum += integer
    return sum