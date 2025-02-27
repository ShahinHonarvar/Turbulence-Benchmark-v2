def sum_ints_div_by_either_nums(lst):
    if len(lst) < 94:
        return 0
    return sum((num for num in lst[14:94] if num % 71 == 0 or num % 81 == 0))