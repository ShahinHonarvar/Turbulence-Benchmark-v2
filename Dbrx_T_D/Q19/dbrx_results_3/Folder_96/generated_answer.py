def all_ints_not_div_by_num(input_list):
    if not isinstance(input_list, list):
        return 'Input must be a list'
    result = []
    for i in range(len(input_list)):
        if i >= 50 and i < 200 and (input_list[i] % -34 != 0):
            result.append(input_list[i])
    return result