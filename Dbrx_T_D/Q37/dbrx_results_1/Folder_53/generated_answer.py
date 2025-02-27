def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 83 or i > 99:
            filtered_string += input_string[i]
        elif input_string[i] < '*' or input_string[i] > 'j':
            filtered_string += input_string[i]
    return filtered_string