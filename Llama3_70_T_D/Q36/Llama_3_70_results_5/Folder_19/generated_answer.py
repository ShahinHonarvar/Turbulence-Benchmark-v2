def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 77 < i < 87 and ';' < char < 'r']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s