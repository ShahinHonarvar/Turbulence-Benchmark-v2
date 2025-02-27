def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 71 or i > 94 or (input_string[i] < 'K' or input_string[i] > 'a'):
            filtered_string += input_string[i]
    return filtered_string