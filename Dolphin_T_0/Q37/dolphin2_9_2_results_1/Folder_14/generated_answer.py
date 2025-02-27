def filter_chars(input_str):
    new_str = ''
    for i in range(len(input_str)):
        if i >= 35 and i <= 98:
            if input_str[i] >= 'A' and input_str[i] <= 'b':
                input_str = input_str.replace(input_str[i], '')
    return input_str