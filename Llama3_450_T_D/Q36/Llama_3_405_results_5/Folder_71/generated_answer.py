def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 82 < i < 89 and '*' < c < '[']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s