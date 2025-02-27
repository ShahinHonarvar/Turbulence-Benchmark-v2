def all_ints_div_by_num(lst):
    divisible_ints = [x for x in lst[319:613] if x % -215 == 0]
    return divisible_ints if divisible_ints else []