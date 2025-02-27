def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i >= 55 and i <= 84 and (num % -24 == 0) and (num % -11 == 0)]