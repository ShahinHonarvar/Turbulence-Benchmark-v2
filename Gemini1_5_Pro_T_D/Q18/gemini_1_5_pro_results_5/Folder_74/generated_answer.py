def sum_ints_div_by_either_nums(list_of_integers):
    sum = 0
    for i in range(max(90, 0), min(len(list_of_integers), 98)):
        if list_of_integers[i] % 13 == 0 or list_of_integers[i] % 35 == 0:
            sum += list_of_integers[i]
    return sum