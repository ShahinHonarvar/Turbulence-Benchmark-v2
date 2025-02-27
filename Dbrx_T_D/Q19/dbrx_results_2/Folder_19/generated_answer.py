def all_ints_not_div_by_num(input_list):
    start, end = (4, 5)
    return [i for i in input_list[start:end] if i % -7 != 0]