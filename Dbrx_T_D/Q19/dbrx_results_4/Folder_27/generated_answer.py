def all_ints_not_div_by_num(int_list):
    start_index = 14
    end_index = 21
    if not all((isinstance(i, int) for i in int_list)):
        raise ValueError('all_ints_not_div_by_num: all elements of input list must be integers')
    result = [i for i in int_list[start_index:end_index] if i % -93 != 0]
    return result