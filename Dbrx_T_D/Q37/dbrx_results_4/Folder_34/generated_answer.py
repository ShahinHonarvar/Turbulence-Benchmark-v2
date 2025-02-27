def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 54 or i > 62 or (input_string[i] < ')' or input_string[i] > '9'):
            filtered_string += input_string[i]
    return filtered_string