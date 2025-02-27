def all_ints_div_by_num(lst, num=6):
    divisible_by_num = [i for i in lst if i % num == 0]
    return divisible_by_num