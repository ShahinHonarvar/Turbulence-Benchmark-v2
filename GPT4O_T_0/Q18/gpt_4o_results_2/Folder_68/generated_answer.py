def sum_ints_div_by_either_nums(lst):
    if len(lst) < 8:
        return 0
    num = lst[7]
    if num % 5 == 0 or num % 7 == 0:
        return num
    return 0