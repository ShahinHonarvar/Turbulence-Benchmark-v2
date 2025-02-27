def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 15 or i > 55:
            filtered_string += input_string[i]
        elif not (input_string[i] >= 'W' and input_string[i] <= '{'):
            filtered_string += input_string[i]
    return filtered_string