def all_ints_div_by_both_two_nums(list_of_integers):
    return [number for index, number in enumerate(list_of_integers) if index in range(138, 425) and number % -863 == 0 and (number % -329 == 0)]