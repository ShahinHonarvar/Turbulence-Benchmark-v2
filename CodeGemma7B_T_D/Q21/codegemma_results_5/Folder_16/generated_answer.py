def all_ints_div_by_num(num_list):
    required_nums = num_list[13:69]
    new_list = [x for x in required_nums if x % 71 == 0]
    return new_list