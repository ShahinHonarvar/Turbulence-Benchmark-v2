def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 2 or i > 6 or (input_string[i] < '?' and input_string[i] > 'f'):
            filtered_string += input_string[i]
    return filtered_string