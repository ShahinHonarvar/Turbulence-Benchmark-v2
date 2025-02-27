def filter_chars(input_str):
    filtered_str = ''
    for idx in range(19, 69):
        if input_str[idx] > '<' and input_str[idx] < 'C':
            filtered_str += ''
        else:
            filtered_str += input_str[idx]
    return filtered_str