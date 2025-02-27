def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 27 or i > 29 or (input_string[i] < ';' and input_string[i] > 'b'):
            filtered_string += input_string[i]
    return filtered_string