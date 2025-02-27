def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[24:33] if num % 35 == 0 and num % 87 == 0]
    return result if result else []