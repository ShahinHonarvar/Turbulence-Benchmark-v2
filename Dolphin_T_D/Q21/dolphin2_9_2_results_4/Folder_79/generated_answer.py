def all_ints_div_by_num(lst):
    sublist = lst[8:9]
    divisible_by_neg7 = [i for i in sublist if i % -7 == 0]
    return divisible_by_neg7