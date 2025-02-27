def all_ints_not_div_by_num(input_list):
    if not isinstance(input_list, list):
        raise ValueError('Function argument must be a list')
    result = []
    for i in range(len(input_list)):
        if i < 35 or i >= 98:
            continue
        if input_list[i] % 41 != 0:
            result.append(input_list[i])
    if not result:
        return result
    return result[35:98]