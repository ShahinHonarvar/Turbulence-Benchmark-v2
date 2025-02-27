def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 38 or i > 69 or (input_string[i] < 'H' or input_string[i] > 'e'):
            filtered_string += input_string[i]
    return filtered_string