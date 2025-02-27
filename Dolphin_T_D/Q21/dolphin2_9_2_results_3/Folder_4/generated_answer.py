def all_ints_div_by_num(lst):
    divisible_by_neg_14 = [i for i in lst[12:93] if i % -14 == 0]
    return divisible_by_neg_14