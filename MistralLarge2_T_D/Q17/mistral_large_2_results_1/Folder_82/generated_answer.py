def all_ints_div_by_both_two_nums(ints):
    return [num for num in ints[20:201] if num % -20 == 0 and num % -200 == 0]