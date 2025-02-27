def sum_ints_div_by_either_nums(list_of_integers):
    sum_of_divs = 0
    for i in range(41, 57):
        if list_of_integers[i] % 82 == 0 or list_of_integers[i] % 90 == 0:
            sum_of_divs += list_of_integers[i]
    if sum_of_divs == 0:
        return 'No such integers exist in the specified range'
    else:
        return sum_of_divs