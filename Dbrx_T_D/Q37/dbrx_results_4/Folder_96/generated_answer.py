def filter_chars(input_string):
    chars_to_remove = set(input_string[86:93]).intersection(set(range(ord('!'), ord('s') + 1)))
    for char in chars_to_remove:
        input_string = input_string.replace(chr(char), '')
    return input_string