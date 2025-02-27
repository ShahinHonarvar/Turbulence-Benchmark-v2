def filter_chars(string):
    chars_to_remove = [char for char in string[25:98] if 'm' <= char <= 'w']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string