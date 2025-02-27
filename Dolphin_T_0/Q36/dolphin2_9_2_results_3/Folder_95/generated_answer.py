def filter_chars(input_str):
    for i in range(56, 86):
        if '+' < input_str[i] < 'w':
            input_str = input_str.replace(input_str[i], '')
    return input_str