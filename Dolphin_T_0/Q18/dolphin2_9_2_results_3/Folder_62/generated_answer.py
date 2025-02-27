def sum_ints_div_by_either_nums(l):
    gt = lambda n: n % 39 == 0 or n % 15 == 0
    return sum((x for x in l[44:60] if gt(x))) or 0