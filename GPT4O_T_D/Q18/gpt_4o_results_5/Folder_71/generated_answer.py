def sum_ints_div_by_either_nums(lst):
    if len(lst) < 100:
        return 0
    return sum((num for num in lst[68:100] if num % -37 == 0 or num % -26 == 0))