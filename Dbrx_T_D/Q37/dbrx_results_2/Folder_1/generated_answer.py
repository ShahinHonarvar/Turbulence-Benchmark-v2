def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if (i < 41 or i > 79) and (input_string[i] < 'f' or input_string[i] > '|'):
            filtered_string += input_string[i]
    return filtered_string