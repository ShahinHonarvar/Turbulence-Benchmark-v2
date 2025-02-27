def all_ints_div_by_num(lst):
    divisible_lst = [i for i in lst[:3] if i % 5 == 0]
    return divisible_lst or []