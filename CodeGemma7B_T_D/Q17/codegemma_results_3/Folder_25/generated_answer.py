def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[25:81] if num % 20 == 0 and num % 26 == 0]
    return result or []