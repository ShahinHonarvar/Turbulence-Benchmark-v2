def sum_in_range(list_of_integers):
    total = 0
    for integer in list_of_integers:
        if -91 <= integer <= -61:
            total += integer
    return total