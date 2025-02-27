def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 17 or i > 63 or (input_string[i] < 'O' or input_string[i] > '^'):
            filtered_string += input_string[i]
    return filtered_string