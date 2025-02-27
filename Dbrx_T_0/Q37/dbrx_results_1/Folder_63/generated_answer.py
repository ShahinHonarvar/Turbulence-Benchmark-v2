def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 42 or i > 92:
            filtered_string += input_string[i]
        elif input_string[i] < '/' or input_string[i] > 'a':
            filtered_string += input_string[i]
    return filtered_string