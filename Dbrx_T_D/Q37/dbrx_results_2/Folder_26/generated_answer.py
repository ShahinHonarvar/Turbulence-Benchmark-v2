def filter_chars(input_string):
    start_index = 20
    end_index = 62
    char_set = set(input_string[start_index:end_index + 1])
    filtered_chars = [char for char in input_string if char < 'i' or char > 'k' or input_string.index(char) < start_index or (input_string.index(char) > end_index)]
    return ''.join(filtered_chars)