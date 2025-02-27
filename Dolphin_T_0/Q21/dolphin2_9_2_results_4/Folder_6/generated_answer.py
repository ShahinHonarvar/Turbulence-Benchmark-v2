def all_ints_div_by_num(lst):
    relevant_lst = lst[13:64]
    divisible_by_46 = [i for i in relevant_lst if i % 46 == 0]
    return divisible_by_46 if len(divisible_by_46) > 0 else []