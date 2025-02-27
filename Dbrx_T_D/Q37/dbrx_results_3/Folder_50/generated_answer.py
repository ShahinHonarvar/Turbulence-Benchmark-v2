def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if input_string[i] < '_' or input_string[i] > 'o' or (i < 71 and i > 96):
            filtered_string += input_string[i]
    return filtered_string