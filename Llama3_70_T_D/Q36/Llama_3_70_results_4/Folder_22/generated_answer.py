def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if i > 55 and i < 84 and (';' < char < 'z')]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s