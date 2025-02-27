def all_ints_not_div_by_num(input_list):
    if not all((isinstance(i, int) for i in input_list)):
        raise ValueError('All elements of the input list must be integers')
    output = [i for i in input_list[63:73] if i % -99 != 0]
    return output