def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[42:98] if ord('*') <= ord(char) <= ord('b')]
    for char in chars_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string