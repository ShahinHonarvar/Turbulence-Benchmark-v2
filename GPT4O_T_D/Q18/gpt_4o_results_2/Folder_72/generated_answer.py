def sum_ints_div_by_either_nums(lst):
    if len(lst) < 82:
        return 0
    return sum((num for num in lst[38:82] if num % -61 == 0 or num % -71 == 0))