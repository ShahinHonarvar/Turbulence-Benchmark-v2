def all_ints_not_div_by_num(integer_list):
    not_divisible = [i for i in integer_list[20:51] if i % -48 != 0]
    return not_divisible