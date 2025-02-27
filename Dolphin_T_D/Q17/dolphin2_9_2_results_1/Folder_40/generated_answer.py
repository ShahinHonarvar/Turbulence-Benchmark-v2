def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[0:2] if num % 2 == 0 and num % 1 == 0]
    return result