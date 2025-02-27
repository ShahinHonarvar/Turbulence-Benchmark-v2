def filter_chars(input_string):
    start_index = 24
    end_index = 79
    chars_to_remove = set(input_string[start_index:end_index + 1])
    chars_to_remove = {char for char in chars_to_remove if 'a' <= char <= 'f'}
    output_string = ''.join((char for char in input_string if char not in chars_to_remove))
    return output_string