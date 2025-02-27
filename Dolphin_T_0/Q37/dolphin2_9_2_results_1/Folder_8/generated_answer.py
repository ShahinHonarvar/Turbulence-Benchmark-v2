def filter_chars(input_string):
    for i in range(41, 87):
        if 'S' <= input_string[i] <= 's':
            input_string = input_string.replace(input_string[i], '')
    return input_string