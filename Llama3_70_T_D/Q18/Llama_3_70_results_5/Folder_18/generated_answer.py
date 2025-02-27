def sum_ints_div_by_either_nums(num_list):
    return sum((i for i in num_list[55:67] if i % 22 == 0 or i % 82 == 0))