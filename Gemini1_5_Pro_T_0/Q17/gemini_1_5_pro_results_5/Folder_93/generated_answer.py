def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i in range(86, 90) and num % -61 == 0 and (num % -79 == 0)]