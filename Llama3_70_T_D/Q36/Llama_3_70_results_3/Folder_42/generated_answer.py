def filter_chars(s):
    chars_to_remove = [char for char in s[42:68] if 't' < char < 'x']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s