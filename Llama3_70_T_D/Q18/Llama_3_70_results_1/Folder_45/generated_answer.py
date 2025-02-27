def sum_ints_div_by_either_nums(num_list):
    return sum((i for i in num_list[30:201] if i % -115 == 0 or i % 115 == 0))