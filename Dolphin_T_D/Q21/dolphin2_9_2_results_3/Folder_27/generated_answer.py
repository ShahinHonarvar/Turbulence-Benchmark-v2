def all_ints_div_by_num(input_list):
    target_range = input_list[25:32]
    divisible_by_neg_69 = [i for i in target_range if i % -69 == 0]
    return divisible_by_neg_69