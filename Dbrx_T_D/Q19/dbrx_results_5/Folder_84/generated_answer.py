def all_ints_not_div_by_num(int_list):
    not_divisible = [i for i in int_list[50:81] if i % 64 != 0]
    return not_divisible