def all_ints_div_by_num(ints_list):
    divisible_by_neg_97 = [int for int in ints_list[25:42] if int % -97 == 0]
    return divisible_by_neg_97 if divisible_by_neg_97 else []