def filter_chars(input_string):
    start_index = 7
    end_index = 8
    chars_to_remove = [char for char in set(input_string[start_index:end_index + 1]) if 'B' <= char <= 'H']
    result_string = ''.join((char if char not in chars_to_remove else '' for char in input_string))
    return result_string