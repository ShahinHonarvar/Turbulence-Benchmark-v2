def all_ints_div_by_both_two_nums(list_of_integers):
    return [number for i, number in enumerate(list_of_integers) if i >= 11 and i <= 76 and (number % -81 == 0) and (number % -94 == 0)]