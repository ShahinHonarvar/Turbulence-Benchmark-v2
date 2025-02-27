def all_ints_div_by_num(int_list):
    return [int_list[i] for i in range(13, min(69, len(int_list))) if int_list[i] % 71 == 0]