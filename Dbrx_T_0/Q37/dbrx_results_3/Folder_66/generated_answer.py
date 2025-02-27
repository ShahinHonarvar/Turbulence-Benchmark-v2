def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 27 or i > 85 or (input_string[i] < 'c' or input_string[i] > 'i'):
            filtered_string += input_string[i]
    return filtered_string