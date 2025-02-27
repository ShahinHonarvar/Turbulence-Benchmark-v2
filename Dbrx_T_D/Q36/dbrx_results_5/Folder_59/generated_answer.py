def filter_chars(input_str):
    filtered_str = ''
    for i in range(len(input_str)):
        if i < 3 or i >= 8 or (input_str[i] > '?' and input_str[i] < 'k'):
            filtered_str += input_str[i]
    return filtered_str