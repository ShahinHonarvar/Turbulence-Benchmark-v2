def sum_ints_div_by_either_nums(l):
    return sum((a for a in l[250:630] if a % 850 == 0 or a % 587 == 0)) or 0