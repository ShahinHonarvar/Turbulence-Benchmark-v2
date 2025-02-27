def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i >= 48 and i <= 76 and (num % -46 == 0) and (num % -82 == 0)]