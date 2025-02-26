def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 69 < i < 97 and 'V' < c < 'j']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s