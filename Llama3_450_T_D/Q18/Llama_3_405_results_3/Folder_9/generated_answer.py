def sum_ints_div_by_either_nums(int_list):
    return sum((i for i in int_list[70:201] if i % 3 == 0 or i % -300 == 0))