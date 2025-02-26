def filter_chars(string):
    chars_to_remove = [char for char in string[43:68] if 't' < char < 'x']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string