def filter_chars(input_string):
    for i in range(20, 70):
        if input_string[i] > '<' and input_string[i] < 'C':
            input_string = input_string.replace(input_string[i], '')
    return input_string