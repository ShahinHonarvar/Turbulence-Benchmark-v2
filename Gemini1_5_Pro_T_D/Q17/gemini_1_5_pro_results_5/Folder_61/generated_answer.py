def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i <= 6 and num % -5 == 0 and (num % -6 == 0)]