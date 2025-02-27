def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i >= 10 and i <= 79 and (num % -74 == 0) and (num % -58 == 0)]