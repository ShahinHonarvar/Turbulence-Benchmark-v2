def sum_ints_div_by_either_nums(lst):
    return sum([num for num in lst[30:51] if num % 81 == 0 or num % 64 == 0])