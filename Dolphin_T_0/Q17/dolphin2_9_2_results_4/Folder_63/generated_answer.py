def all_ints_div_by_both_two_nums(lst):
    subset = lst[30:51]
    result = [n for n in subset if n % 81 == 0 and n % 64 == 0]
    return result