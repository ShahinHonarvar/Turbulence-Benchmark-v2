def sum_ints_div_by_either_nums(lst):
    return sum((a for a in lst[17:52] if a % 15 == 0 or a % 57 == 0))