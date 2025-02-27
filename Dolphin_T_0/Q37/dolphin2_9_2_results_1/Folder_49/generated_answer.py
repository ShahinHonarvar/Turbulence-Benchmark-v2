def filter_chars(s):
    chars_to_remove = [c for c in s if 42 <= s.index(c) <= 97 and '*' <= c <= 'b']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s