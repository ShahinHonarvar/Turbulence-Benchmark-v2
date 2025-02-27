def filter_chars(s):
    chars_to_filter = [c for i, c in enumerate(s) if 1 < i < 9 and '8' < c < 'm']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s