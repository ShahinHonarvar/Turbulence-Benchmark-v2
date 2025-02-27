def sum_ints_div_by_either_nums(lst):
    return sum([num for num in lst[13:76] if num % 66 == 0 or num % 32 == 0]) or 0