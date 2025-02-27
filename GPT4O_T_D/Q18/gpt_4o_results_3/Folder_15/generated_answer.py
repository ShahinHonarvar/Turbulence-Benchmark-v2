def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 3:
        range_list = int_list
    else:
        range_list = int_list[:3]
    return sum((x for x in range_list if x % -2 == 0 or x % 3 == 0))