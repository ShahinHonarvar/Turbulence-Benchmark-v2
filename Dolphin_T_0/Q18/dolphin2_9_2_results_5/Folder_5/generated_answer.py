def sum_ints_div_by_either_nums(list_of_ints):
    return sum([num for num in list_of_ints[0:2] if num % -6 == 0 or num % 4 == 0])