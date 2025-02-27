def all_ints_not_div_by_num(int_list):
    num = int_list[0]
    return [i for i in int_list[1:num] if i % num != 0]