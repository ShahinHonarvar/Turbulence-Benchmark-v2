def all_ints_div_by_both_two_nums(list_of_integers):
    return [number for number in list_of_integers[0:1] if number % 1 == 0 and number % -1 == 0]