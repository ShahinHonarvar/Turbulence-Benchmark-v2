def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 421 or i >= 854 or (not (input_string[i] > 'D' and input_string[i] < 'J')):
            filtered_string += input_string[i]
    return filtered_string