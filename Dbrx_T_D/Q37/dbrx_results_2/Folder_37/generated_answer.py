def filter_chars(input_string):
    chars_to_filter = [c for c in input_string[17:63] if ord('O') <= ord(c) <= ord('^')]
    for c in chars_to_filter:
        input_string = input_string.replace(c, '', 1)
    return input_string