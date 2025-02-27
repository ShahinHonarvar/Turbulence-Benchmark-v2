def all_ints_not_div_by_num(input_list, div_num):
    if not isinstance(input_list, list):
        raise TypeError('The input_list argument must be a list.')
    if not all((isinstance(i, int) for i in input_list)):
        raise TypeError('All elements in the input_list argument must be integers.')
    if not isinstance(div_num, int):
        raise TypeError('The div_num argument must be an integer.')
    result = [i for i in input_list[1:3] if i % div_num != 0]
    return result if result else []