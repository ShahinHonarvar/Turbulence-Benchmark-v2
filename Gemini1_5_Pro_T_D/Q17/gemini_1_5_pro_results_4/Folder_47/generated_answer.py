def all_ints_div_by_both_two_nums(list_of_integers):
    return [number for index, number in enumerate(list_of_integers) if index >= 42 and index <= 87 and (number % -90 == 0) and (number % -74 == 0)]