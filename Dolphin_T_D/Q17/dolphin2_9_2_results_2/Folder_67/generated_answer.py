def all_ints_div_by_both_two_nums(int_list):
    range_list = int_list[24:33]
    div_nums = [i for i in range_list if i % 35 == 0 and i % 87 == 0]
    return div_nums