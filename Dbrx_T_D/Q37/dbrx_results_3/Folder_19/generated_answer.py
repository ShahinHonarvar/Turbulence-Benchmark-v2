def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 35 or i > 89 or (input_string[i] < 'E' or input_string[i] > 't'):
            filtered_string += input_string[i]
    return filtered_string