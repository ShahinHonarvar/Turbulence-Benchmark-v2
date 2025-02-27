def filter_chars(string):
    chars_to_remove = [char for char in string[19:23] if ']' <= char <= 't']
    for char in chars_to_remove:
        string = string.replace(char, '', 1)
    return string