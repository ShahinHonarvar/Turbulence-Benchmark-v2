def all_ints_div_by_num(lst):
    divisible_by_91 = [x for x in lst[33:36] if x % 91 == 0]
    return divisible_by_91 if divisible_by_91 else []