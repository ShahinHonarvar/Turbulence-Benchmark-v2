def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 5 or i > 6 or (input_string[i] < 'G' or input_string[i] > 'p'):
            filtered_string += input_string[i]
    return filtered_string