def filter_chars(input_str):
    result_str = ''
    for i in range(len(input_str)):
        if i < 331 or i > 713 or (input_str[i] <= 'M' and input_str[i] >= '_'):
            result_str += input_str[i]
    return result_str