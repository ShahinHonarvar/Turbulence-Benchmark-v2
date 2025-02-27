def sum_ints_div_by_either_nums(lst):
    total = sum((x for x in lst[200:30:-1] if x % -115 == 0 or x % 115 == 0))
    return total if total else 0