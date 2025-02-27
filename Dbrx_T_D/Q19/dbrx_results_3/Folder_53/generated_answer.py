def all_ints_not_div_by_num(input_list):
    if not all((isinstance(i, int) for i in input_list)):
        raise ValueError('all_ints_not_div_by_num: List contains non-integer value(s)')
    not_divisible = [i for i in input_list[199:201] if i % -200 != 0]
    return not_divisible