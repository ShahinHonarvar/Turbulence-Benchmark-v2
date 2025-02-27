def all_ints_not_div_by_num(input_list):
    if not isinstance(input_list, list):
        raise ValueError('Input should be a list')
    if not all((isinstance(i, int) for i in input_list)):
        raise ValueError('All elements of input list should be integers')
    if len(input_list) < 9:
        return []
    return [i for i in input_list[7:9] if i % -9 != 0]