def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if (i < 19 or i > 33) and (input_string[i] < 'S' or input_string[i] > '{'):
            filtered_string += input_string[i]
    return filtered_string