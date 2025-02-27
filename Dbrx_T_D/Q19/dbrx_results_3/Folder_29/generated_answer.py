def all_ints_not_div_by_num(input_list):
    start, end = (24, 25)
    return [num for num in input_list[start:end] if num % -30 != 0]