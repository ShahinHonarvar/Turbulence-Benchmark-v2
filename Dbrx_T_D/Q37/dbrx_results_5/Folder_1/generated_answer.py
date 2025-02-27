def filter_chars(input_str):
    filtered_str = ''
    for i in range(len(input_str)):
        if (i < 41 or i > 79) or (input_str[i] < 'f' or input_str[i] > '|'):
            filtered_str += input_str[i]
    return filtered_str