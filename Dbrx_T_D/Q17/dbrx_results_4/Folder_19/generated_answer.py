def all_ints_div_by_both_two_nums(my_list):
    sublist = my_list[1:5]
    result = [i for i in sublist if i % 4 == 0 and i % -6 == 0]
    return result