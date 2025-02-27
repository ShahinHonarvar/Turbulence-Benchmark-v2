def filter_chars(input_string):
    lower_bound = 19
    upper_bound = 90
    chars_to_remove = [char for char in set(input_string[lower_bound:upper_bound + 1]) if 'F' <= char <= 'h']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string