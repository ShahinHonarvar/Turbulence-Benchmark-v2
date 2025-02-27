def sum_ints_div_by_either_nums(lst):
    if len(lst) < 76:
        return 0
    return sum((num for num in lst[58:76] if num % 72 == 0 or num % 62 == 0))