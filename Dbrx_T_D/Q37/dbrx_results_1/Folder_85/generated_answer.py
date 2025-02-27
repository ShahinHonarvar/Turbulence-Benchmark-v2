def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 28 or i > 65 or (input_string[i] < 'O' or input_string[i] > 'd'):
            filtered_string += input_string[i]
    return filtered_string