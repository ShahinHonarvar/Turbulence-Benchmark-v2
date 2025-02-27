def filter_chars(input_string):
    chars_to_remove = set(input_string[515:539])
    for char in chars_to_remove:
        if ord(char) >= ord('+') and ord(char) <= ord('}'):
            input_string = input_string.replace(char, '')
    return input_string