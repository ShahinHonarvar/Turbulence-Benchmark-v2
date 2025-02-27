def all_ints_div_by_both_two_nums(list_of_integers):
    return [number for i in range(38, 82) for number in list_of_integers[i:i + 1] if number % -61 == 0 and number % -71 == 0]