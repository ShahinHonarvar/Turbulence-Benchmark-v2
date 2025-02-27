def filter_chars(input_string):
    chars_to_remove = set(input_string[37:57]).intersection(set(range(ord('6'), ord('_') + 1)))
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string