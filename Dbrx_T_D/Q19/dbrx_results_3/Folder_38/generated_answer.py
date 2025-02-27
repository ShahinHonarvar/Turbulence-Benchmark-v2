def all_ints_not_div_by_num(integer_list):
    start_index = 32
    end_index = 54
    result = [int for int in integer_list[start_index:end_index] if int % -97 != 0]
    return result