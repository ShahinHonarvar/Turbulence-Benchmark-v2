def all_ints_not_div_by_num(integer_list):
    start = 33
    end = 78
    return [i for i in integer_list[start:end] if i % -17 != 0]