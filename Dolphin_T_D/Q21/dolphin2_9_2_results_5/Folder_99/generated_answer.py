def all_ints_div_by_num(int_list, num=763, start_index=161, end_index=970):
    divisible_nums = [i for i in int_list[start_index:end_index + 1] if i % num == 0]
    return divisible_nums