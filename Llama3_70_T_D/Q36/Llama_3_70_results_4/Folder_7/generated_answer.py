def filter_chars(s):
    chars_to_remove = [c for c in s[502:946] if 'W' < c < 'y']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s