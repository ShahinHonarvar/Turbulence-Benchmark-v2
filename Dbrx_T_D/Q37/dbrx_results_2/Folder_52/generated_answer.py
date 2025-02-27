def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 54 or i > 83 or (i >= 54 and i <= 83 and (input_string[i] < 'j' or input_string[i] > 'v')):
            filtered_string += input_string[i]
    return filtered_string