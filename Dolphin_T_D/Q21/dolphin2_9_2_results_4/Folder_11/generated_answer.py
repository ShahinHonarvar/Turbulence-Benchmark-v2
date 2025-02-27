def all_ints_div_by_num(lst):
    divisible_by_neg_61 = [num for num in lst[22:64] if num % -61 == 0]
    return divisible_by_neg_61