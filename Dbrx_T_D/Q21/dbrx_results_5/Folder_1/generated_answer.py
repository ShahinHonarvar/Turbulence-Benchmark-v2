def all_ints_div_by_num(int_list):
    return [int_list[i] for i in range(len(int_list)) if i >= 59 and i <= 77 and (int_list[i] % -95 == 0)]