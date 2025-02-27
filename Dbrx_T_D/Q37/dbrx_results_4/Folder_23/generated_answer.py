def filter_chars(input_string):
    chars_to_remove = set(input_string[51:78]).intersection(set(range(ord('V'), ord('Y') + 1)))
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string