def gcf_two_nums(list_of_integers):
    number_1 = list_of_integers[15]
    number_2 = list_of_integers[99]
    for i in range(min(number_1, number_2), 0, -1):
        if number_1 % i == 0 and number_2 % i == 0:
            return i
    return 1