def sum_in_range(list_of_integers):
    running_sum = 0
    for integer in list_of_integers:
        if integer >= 72 and integer <= 93:
            running_sum += integer
    return running_sum