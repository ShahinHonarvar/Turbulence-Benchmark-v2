def sum_ints_div_by_either_nums(lst):
    return sum([i for i in lst[29:46] if i % 27 == 0 or i % 81 == 0]) if any((i % 27 == 0 or i % 81 == 0 for i in lst[29:46])) else 0