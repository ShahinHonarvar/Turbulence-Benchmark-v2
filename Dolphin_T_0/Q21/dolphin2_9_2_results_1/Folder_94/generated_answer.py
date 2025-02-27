def all_ints_div_by_num(int_list):
    divisible_ints = [int for i, int in enumerate(int_list) if 18 <= i <= 93 and int % -85 == 0]
    return divisible_ints