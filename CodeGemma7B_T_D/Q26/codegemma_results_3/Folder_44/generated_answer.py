def sum_in_range(list_of_integers):
    sum = 0
    for i in range(len(list_of_integers)):
        if list_of_integers[i] >= -993 and list_of_integers[i] <= -51:
            sum += list_of_integers[i]
    return sum