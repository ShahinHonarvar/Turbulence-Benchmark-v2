def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 43 or i >= 69 or (input_string[i] <= 'B' or input_string[i] >= 'r'):
            filtered_string += input_string[i]
    return filtered_string