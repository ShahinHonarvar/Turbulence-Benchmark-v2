def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[40:201] if num % 21 == 0 and num % 71 == 0]
    return result if result else []