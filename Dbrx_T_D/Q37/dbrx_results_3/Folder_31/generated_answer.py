def filter_chars(s):
    chars_to_remove = [c for c in s if 57 <= ord(c) <= 96 and c >= '<' and (c <= 'w')]
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s