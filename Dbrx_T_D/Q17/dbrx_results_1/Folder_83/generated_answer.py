def all_ints_div_by_both_two_nums(int_list):
    return [int_list[i] for i in range(90, 201) if int_list[i] % -31 == 0 and int_list[i] % 13 == 0]