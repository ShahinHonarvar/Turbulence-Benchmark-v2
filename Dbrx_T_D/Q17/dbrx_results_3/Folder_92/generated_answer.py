def all_ints_div_by_both_two_nums(input_list):
    return [i for i in input_list if i % 1 == 0 and i % -1 == 0 and (0 <= i <= input_list[0])]