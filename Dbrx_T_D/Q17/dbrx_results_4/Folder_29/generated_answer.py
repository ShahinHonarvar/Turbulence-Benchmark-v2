def all_ints_div_by_both_two_nums(lst):
    start, end = (55, 84)
    result = [num for num in lst[start:end + 1] if num % -24 == 0 and num % -11 == 0]
    return result