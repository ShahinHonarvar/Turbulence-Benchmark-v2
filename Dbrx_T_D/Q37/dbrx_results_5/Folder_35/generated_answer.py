def filter_chars(input_string):
    chars_to_remove = set(input_string[155:403]).intersection(range(40, 93))
    for char in chars_to_remove:
        input_string = input_string.replace(chr(char), '')
    return input_string