def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[25:96] if num % 51 == 0 and num % 77 == 0]
    return result if result else []