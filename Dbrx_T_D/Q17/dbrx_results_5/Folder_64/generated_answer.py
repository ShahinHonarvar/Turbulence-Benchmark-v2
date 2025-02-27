def all_ints_div_by_both_two_nums(lst):
    div_by_11 = [num for num in lst[0:4] if num % 11 == 0]
    div_by_11_and_7 = [num for num in div_by_11 if num % -7 == 0]
    return div_by_11_and_7