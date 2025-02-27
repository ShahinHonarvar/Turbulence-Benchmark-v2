def sum_ints_div_by_either_nums(my_list):
    return sum((i for i in my_list[18:53] if i % 15 == 0 or i % 57 == 0))