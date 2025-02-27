def sum_in_range(list_of_integers):
    result = 0
    for integer in list_of_integers:
        if integer >= 68 and integer <= 99:
            result += integer
    return result