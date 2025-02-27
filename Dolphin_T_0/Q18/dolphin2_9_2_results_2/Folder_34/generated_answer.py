def sum_ints_div_by_either_nums(lst):
    if 200 >= len(lst) >= 60:
        return sum([x for x in lst[60:201] if x % 9 == 0 or x % 11 == 0])
    else:
        return 0