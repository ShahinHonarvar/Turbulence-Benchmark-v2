def filter_chars(s):
    chars_to_remove = [c for c in s[15:55] if 'W' <= c <= '{']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s