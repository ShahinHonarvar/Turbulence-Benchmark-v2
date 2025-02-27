def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i >= 50 and i <= 92 and (num % -94 == 0) and (num % -95 == 0)]