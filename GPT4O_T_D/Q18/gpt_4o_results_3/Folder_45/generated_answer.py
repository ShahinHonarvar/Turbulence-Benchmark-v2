def sum_ints_div_by_either_nums(lst):
    if not lst or len(lst) < 31:
        return 0
    return sum((num for num in lst[30:201] if num % 115 == 0))