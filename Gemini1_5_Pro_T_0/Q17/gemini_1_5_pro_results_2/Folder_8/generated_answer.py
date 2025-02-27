def all_ints_div_by_both_two_nums(list_of_integers):
    return [number for index, number in enumerate(list_of_integers) if index >= 36 and index <= 85 and (number % -27 == 0) and (number % -96 == 0)]