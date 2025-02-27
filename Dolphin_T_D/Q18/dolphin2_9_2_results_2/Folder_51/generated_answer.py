def sum_ints_div_by_either_nums(int_list):
    sublist = int_list[6:10]
    result = sum((i for i in sublist if i % -1 == 0 or i % -10 == 0))
    return result if result else 0