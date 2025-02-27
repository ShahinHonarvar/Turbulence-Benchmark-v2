def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 34 or i > 67 or (input_string[i] < 'W' or input_string[i] > 'x'):
            filtered_string += input_string[i]
    return filtered_string