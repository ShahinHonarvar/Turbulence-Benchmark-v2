def filter_chars(s):
    chars_to_remove = [c for c in s[38:55] if c >= ':' and c <= 'r']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s