def all_ints_div_by_both_two_nums(lst):
    div_by_275_580 = [num for num in lst[153:799] if num % 275 == 0 and num % 580 == 0]
    return div_by_275_580