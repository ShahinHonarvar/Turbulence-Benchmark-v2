def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 72 or i > 94 or (input_string[i] < '.' or input_string[i] > 'b'):
            filtered_string += input_string[i]
    return filtered_string