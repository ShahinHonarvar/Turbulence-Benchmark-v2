def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    for i in range(max(3, 0), min(len(list_of_integers), 10)):
        if list_of_integers[i] % 6 == 0 or list_of_integers[i] % 1 == 0:
            sum += list_of_integers[i]
    return sum