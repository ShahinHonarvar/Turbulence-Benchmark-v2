def filter_chars(string):
    chars_to_remove = [char for char in string[27:86] if 'c' <= char <= 'i']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string