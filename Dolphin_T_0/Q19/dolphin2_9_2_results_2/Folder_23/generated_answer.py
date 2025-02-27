def all_ints_not_div_by_num(list_of_integers):
    divisible_by_neg_68 = [i for i in list_of_integers[44:91] if i % -68 != 0]
    return divisible_by_neg_68 if any(divisible_by_neg_68) else []