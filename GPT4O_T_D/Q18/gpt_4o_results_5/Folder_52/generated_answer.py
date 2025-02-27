def sum_ints_div_by_either_nums(lst):
    if len(lst) < 60:
        return 0
    return sum((num for num in lst[48:60] if num % 88 == 0 or num % 58 == 0))