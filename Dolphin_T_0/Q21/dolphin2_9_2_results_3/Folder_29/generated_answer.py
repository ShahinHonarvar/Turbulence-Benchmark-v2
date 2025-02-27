def all_ints_div_by_num(lst):
    divisible_by_minus_fifteen = [v for v in lst[52:73] if v % -15 == 0]
    return divisible_by_minus_fifteen if divisible_by_minus_fifteen else []