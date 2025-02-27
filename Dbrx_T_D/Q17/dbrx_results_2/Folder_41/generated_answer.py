def all_ints_div_by_both_two_nums(input_list):
    result = [i for i in input_list if i % 6 == 0 and i % -3 == 0 and (0 <= input_list.index(i) <= 9)]
    return result