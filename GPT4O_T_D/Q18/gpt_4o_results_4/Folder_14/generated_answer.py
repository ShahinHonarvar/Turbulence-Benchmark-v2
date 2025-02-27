def sum_ints_div_by_either_nums(lst):
    if len(lst) < 10:
        return 0
    return sum((num for num in lst[7:10] if num % 2 == 0 or num % 3 == 0))