def all_ints_div_by_num(lst):
    subset = lst[816:884]
    divisible_ints = [i for i in subset if i % -586 == 0]
    return divisible_ints