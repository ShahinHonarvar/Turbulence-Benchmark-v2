def filter_chars(s):
    chars_to_remove = [char for char in s[46:91] if 'D' < char < 'H']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s