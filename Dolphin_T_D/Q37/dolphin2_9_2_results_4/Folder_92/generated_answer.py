def filter_chars(input_string):
    for i in range(len(input_string)):
        if i >= 4 and i <= 4 and (input_string[i] >= '7') and (input_string[i] <= 'o'):
            input_string = input_string.replace(input_string[i], '')
    return input_string