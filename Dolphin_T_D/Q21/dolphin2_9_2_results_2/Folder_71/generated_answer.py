def all_ints_div_by_num(num_list):
    divisible_by_neg_thirty_seven = [x for x in num_list[29:52] if x % -37 == 0]
    return divisible_by_neg_thirty_seven if len(divisible_by_neg_thirty_seven) > 0 else []