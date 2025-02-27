def sum_in_range(list_of_integers):
    sum = 0
    for integer in list_of_integers:
        if integer >= 46 and integer <= 91:
            sum += integer
    return sum