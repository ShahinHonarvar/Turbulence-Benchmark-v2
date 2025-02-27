def all_ints_div_by_both_two_nums(lst):
    divisible_by_1 = [i for i in lst if i % 1 == 0]
    divisible_by_neg_1 = [i for i in lst if i % -1 == 0]
    result = list(set(divisible_by_1) & set(divisible_by_neg_1))
    return result