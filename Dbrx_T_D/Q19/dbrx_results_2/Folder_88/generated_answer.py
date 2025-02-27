def all_ints_not_div_by_num(input_list):
    if not isinstance(input_list, list):
        raise TypeError('Input should be a list')
    if not all((isinstance(i, int) for i in input_list)):
        raise TypeError('All elements of input list should be integers')
    if not input_list[4:8]:
        raise IndexError('Input list should have at least 8 elements')
    if not all((0 <= i <= len(input_list) - 1 for i in (4, 7))):
        raise IndexError('Invalid range specified')
    return [i for i in input_list[4:8] if i % -6 != 0]