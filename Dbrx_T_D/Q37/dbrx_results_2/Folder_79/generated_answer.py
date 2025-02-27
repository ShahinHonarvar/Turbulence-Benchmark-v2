def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 10 or i > 52 or (input_string[i] < '@' or input_string[i] > 'T'):
            filtered_string += input_string[i]
    return filtered_string