def sum_ints_div_by_either_nums(lst):
    if len(lst) < 201:
        return 0
    num = lst[200]
    return num if num % 17 == 0 or num % -5 == 0 else 0