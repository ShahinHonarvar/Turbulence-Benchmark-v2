def all_ints_div_by_both_two_nums(lst):
    return [num for num in lst[:10] if num % 100 == 0 and num % 10 == 0]