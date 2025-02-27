def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if integer >= 77 and integer <= 84:
            sum += integer
    return sum