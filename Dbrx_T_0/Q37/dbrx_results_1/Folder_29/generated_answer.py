def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 12 or i > 87 or (input_string[i] < '&' or input_string[i] > 'v'):
            filtered_string += input_string[i]
    return filtered_string