def all_ints_div_by_both_two_nums(list_of_integers):
    return [number for index, number in enumerate(list_of_integers) if index >= 57 and index <= 84 and (number % -30 == 0) and (number % -88 == 0)]