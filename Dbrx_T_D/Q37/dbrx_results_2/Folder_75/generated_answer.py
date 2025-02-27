def filter_chars(input_string):
    filtered_string = ''
    start_index = 34
    end_index = 67
    for i, char in enumerate(input_string):
        if (char < 'W' or char > 'x') or i < start_index or i > end_index:
            filtered_string += char
    return filtered_string