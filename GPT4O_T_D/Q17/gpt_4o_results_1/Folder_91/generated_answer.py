def all_ints_div_by_both_two_nums(integers):
    return [n for n in integers[:5] if n % 8 == 0 and n % -3 == 0]