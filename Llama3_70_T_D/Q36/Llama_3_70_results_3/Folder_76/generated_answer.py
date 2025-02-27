def filter_chars(s):
    chars_to_remove = [char for char in s[669:888] if 'B' < char < 'Y']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s