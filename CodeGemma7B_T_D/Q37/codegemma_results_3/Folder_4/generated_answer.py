def filter_chars(input_str):
    filtered_str = list(input_str)
    for i in range(19, 34):
        if input_str[i] >= 'S' and input_str[i] <= '{':
            filtered_str.remove(input_str[i])
    return ''.join(filtered_str)