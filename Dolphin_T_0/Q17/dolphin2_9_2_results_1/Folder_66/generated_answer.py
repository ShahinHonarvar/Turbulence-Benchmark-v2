def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[57:82] if num % 55 == 0 and num % 10 == 0]
    return result