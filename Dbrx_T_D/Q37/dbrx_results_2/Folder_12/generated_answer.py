def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 19 or i > 90:
            filtered_string += input_string[i]
        elif input_string[i] < 'F' or input_string[i] > 'h':
            filtered_string += input_string[i]
    return filtered_string