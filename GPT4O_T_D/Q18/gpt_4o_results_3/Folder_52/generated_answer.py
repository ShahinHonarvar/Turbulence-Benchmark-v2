def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 60:
        return 0
    return sum((i for i in int_list[48:60] if i % 88 == 0 or i % 58 == 0))