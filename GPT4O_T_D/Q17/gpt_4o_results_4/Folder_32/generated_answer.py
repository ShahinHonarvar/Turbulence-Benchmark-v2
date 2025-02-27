def all_ints_div_by_both_two_nums(lst):
    start, end = (25, 96)
    return [num for num in lst[start:end] if num % 51 == 0 and num % 77 == 0]