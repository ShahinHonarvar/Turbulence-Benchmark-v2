def filter_chars(input_string):
    start_index = 13
    end_index = 28
    chars_to_remove = [c for c in input_string[start_index:end_index + 1] if 'c' <= c <= 'n']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string