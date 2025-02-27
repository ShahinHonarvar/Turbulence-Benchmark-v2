def all_ints_div_by_both_two_nums(int_list):
    return [int(i) for i in int_list[31:51] if int(i) % 81 == 0 and int(i) % 64 == 0]