def sum_ints_div_by_either_nums(int_list):
    return sum((x for x in int_list[80:201] if x % 10 == 0 or x % 1000 == 0))