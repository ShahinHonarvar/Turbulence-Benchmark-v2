def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 114 or i > 639 or (input_string[i] < '!' or input_string[i] > 'x'):
            filtered_string += input_string[i]
    return filtered_string