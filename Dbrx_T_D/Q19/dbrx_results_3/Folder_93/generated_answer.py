def all_ints_not_div_by_num(input_list):
    if not isinstance(input_list, list):
        raise ValueError('Input must be a list')
    result = []
    for i in range(33, 78):
        if i >= len(input_list):
            break
        if input_list[i] % -17 != 0:
            result.append(input_list[i])
    return result