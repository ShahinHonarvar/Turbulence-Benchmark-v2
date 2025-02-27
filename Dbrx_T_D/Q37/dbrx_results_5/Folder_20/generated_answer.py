def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 25 or i > 97 or (input_string[i] < 'm' or input_string[i] > 'w'):
            filtered_string += input_string[i]
    return filtered_string