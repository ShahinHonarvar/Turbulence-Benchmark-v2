def filter_chars(input_str):
    result_str = ''
    for i in range(len(input_str)):
        if i < 26 or i > 64 or (input_str[i] < 'V' or input_str[i] > 'o'):
            result_str += input_str[i]
    return result_str