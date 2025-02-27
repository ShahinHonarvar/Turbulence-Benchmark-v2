def sum_ints_div_by_either_nums(int_list):
    return sum((i for i in int_list[20:94] if i % -92 == 0 or i % -50 == 0))