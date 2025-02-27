def all_ints_not_div_by_num(integer_list):
    start_index = 41
    end_index = 69
    nums_not_div = [i for i in integer_list[start_index:end_index] if i % -82 != 0]
    return nums_not_div