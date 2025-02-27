def sum_ints_div_by_either_nums(lst):
    if not lst or len(lst) < 425:
        return 0
    return sum((x for x in lst[138:425] if x % -863 == 0 or x % -329 == 0))