def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[20:201] if x % 20 == 0 or x % 200 == 0))