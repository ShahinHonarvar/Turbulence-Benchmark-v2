def all_ints_not_div_by_num(input_list):
    if not isinstance(input_list, list):
        raise TypeError('Input should be a list')
    result = []
    for i in range(361, 887):
        if i < len(input_list) and input_list[i] % 877 != 0:
            result.append(input_list[i])
    return result