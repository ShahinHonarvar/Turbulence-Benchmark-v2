def filter_chars(input_string):
    for i in range(3, 5):
        if input_string[i] > 'Y' and input_string[i] < 's':
            input_string = input_string.replace(input_string[i], '')
    return input_string