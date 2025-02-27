def all_ints_not_div_by_num(input_list):
    if not isinstance(input_list, list):
        return 'The input must be a list of integers.'
    result = []
    for i in range(len(input_list)):
        if i >= 56 and i < 88 and (input_list[i] % -59 != 0):
            result.append(input_list[i])
    return result