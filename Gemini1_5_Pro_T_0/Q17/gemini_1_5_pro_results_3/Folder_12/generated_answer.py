def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i >= 35 and i <= 64 and (num % -30 == 0) and (num % -95 == 0)]