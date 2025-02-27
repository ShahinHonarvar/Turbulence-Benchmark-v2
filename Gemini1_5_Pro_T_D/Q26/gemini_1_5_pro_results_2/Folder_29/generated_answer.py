def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if integer >= 18 and integer <= 60:
            sum += integer
    return sum