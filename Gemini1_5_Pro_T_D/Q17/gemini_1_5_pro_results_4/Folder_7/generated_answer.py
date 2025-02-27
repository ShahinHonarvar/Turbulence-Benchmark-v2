def all_ints_div_by_both_two_nums(list_of_integers):
    return [number for index, number in enumerate(list_of_integers) if index in range(543, 585) and number % -553 == 0 and (number % -737 == 0)]