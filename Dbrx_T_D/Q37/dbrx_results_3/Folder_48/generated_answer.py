def filter_chars(input_string):
    start_index = 513
    end_index = 877
    min_char = '>'
    max_char = 'n'
    filtered_chars = [char for i, char in enumerate(input_string) if i < start_index or i > end_index or (char < min_char or char > max_char)]
    return ''.join(filtered_chars)