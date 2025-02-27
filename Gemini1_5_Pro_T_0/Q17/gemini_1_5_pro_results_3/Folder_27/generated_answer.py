def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i in range(20, 36) and num % -36 == 0 and (num % -89 == 0)]