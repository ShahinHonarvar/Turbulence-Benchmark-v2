def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 75 or i > 99 or (input_string[i] < '8' or input_string[i] > 'e'):
            filtered_string += input_string[i]
    return filtered_string