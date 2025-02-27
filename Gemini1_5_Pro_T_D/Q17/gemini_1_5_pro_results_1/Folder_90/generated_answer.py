def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i, num in enumerate(list_of_ints) if i >= 138 and i <= 424 and (num % -863 == 0) and (num % -329 == 0)]