def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i >= 70 and i <= 200 and (num % 3 == 0) and (num % -300 == 0)]