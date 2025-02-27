def all_ints_div_by_both_two_nums(list_of_integers):
    return [number for i, number in enumerate(list_of_integers) if i in range(10, 80) and number % -74 == 0 and (number % -58 == 0)]