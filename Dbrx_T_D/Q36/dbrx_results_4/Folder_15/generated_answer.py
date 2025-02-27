def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 2 or i >= 7 or (input_string[i] < 'h' or input_string[i] > 'k'):
            filtered_string += input_string[i]
    return filtered_string