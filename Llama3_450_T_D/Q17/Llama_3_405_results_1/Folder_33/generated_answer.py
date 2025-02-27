def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[281:695] if num % -722 == 0 and num % -731 == 0]
    return result