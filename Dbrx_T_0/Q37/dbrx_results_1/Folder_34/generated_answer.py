def filter_chars(input_string):
    chars_to_remove = set(input_string[54:63]).intersection(set(range(ord(')'), ord('9') + 1)))
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string