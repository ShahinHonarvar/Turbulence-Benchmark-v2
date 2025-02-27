def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if 240 <= i <= 901 and (x % 546 == 0 or x % 709 == 0)))