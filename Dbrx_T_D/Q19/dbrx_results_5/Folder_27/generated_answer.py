def all_ints_not_div_by_num(input_list):
    if not all((isinstance(i, int) for i in input_list)):
        raise ValueError('Input list must contain only integers')
    result = [i for i in input_list[13:20] if i % -93 != 0]
    if len(result) < 4:
        raise IndexError('Not enough integers not divisible by -93 in the specified range')
    return result