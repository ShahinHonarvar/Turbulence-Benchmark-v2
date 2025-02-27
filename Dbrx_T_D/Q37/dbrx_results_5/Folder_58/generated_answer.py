def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 503 or i > 753 or (input_string[i] < '9' or input_string[i] > 'w'):
            filtered_string += input_string[i]
    return filtered_string