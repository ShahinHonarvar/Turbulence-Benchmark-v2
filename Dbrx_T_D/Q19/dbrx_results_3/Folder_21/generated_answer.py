def all_ints_not_div_by_num(input_list):
    if not isinstance(input_list, list):
        raise ValueError('Input must be a list')
    result = [i for i in input_list[469:566] if i % -692 != 0]
    return result