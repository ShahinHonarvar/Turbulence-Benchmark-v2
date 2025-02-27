def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i >= 42 and i <= 87 and (num % -90 == 0) and (num % -74 == 0)]