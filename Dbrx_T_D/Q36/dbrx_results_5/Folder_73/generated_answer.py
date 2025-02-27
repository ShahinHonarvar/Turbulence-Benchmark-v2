def filter_chars(string):
    chars_to_remove = set(string[66:90]).intersection(range(ord('#') + 1, ord('T')))
    for char in chars_to_remove:
        string = string.replace(chr(char), '')
    return string