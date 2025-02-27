def sum_ints_div_by_either_nums(lst):
    if len(lst) < 200:
        return 0
    return sum((x for x in lst[80:201] if x % 10 == 0 or x % 1000 == 0))