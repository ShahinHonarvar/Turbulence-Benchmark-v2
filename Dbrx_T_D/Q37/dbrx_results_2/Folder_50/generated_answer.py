def filter_chars(input_string):
    chars_to_remove = [char for char in input_string if ord('_') <= ord(char) <= ord('o') and 70 < input_string.index(char) < 97]
    for char in chars_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string