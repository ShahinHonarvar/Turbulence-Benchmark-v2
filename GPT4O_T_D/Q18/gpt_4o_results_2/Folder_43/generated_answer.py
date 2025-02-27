def sum_ints_div_by_either_nums(lst):
    if not lst or len(lst) < 86:
        return 0
    return sum((num for num in lst[57:86] if num % -77 == 0 or num % -32 == 0))