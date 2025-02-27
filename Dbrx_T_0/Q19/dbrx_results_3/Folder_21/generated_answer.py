def all_ints_not_div_by_num(input_list):
    if not isinstance(input_list, list):
        raise ValueError('Input must be a list')
    if not all((isinstance(i, int) for i in input_list)):
        raise ValueError('All elements of input list must be integers')
    result = [i for i in input_list[469:566] if i % -692 != 0]
    return result