def sum_ints_div_by_either_nums(num_list):
    return sum((x for x in num_list[34:70] if x % 19 == 0 or x % 32 == 0))