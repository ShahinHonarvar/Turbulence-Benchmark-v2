def filter_chars(input_string):
    start_index = 55
    end_index = 66
    filtered_string = ''
    for index, char in enumerate(input_string):
        if not (start_index < index < end_index and 'f' < char < '|'):
            filtered_string += char
    return filtered_string