def filter_chars(s):
    chars_to_remove = set(s[37:57].replace('_', '').replace('`', ''))
    chars_to_remove = [char for char in chars_to_remove if '6' <= char <= '_']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s