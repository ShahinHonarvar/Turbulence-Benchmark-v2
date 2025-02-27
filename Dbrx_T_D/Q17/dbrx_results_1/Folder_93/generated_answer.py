def all_ints_div_by_both_two_nums(int_list):
    return [int_list[i] for i in range(len(int_list)) if i in [86, 87, 88, 89] and int_list[i] % -61 == 0 and (int_list[i] % -79 == 0)]