def sum_ints_div_by_either_nums(lst):
    if len(lst) < 98:
        return 0
    return sum((num for num in lst[69:98] if num % -90 == 0 or num % -67 == 0))