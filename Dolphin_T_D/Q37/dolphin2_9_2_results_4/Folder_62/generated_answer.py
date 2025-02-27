def filter_chars(s):
    chars_to_filter = [c for c in s[10:70] if 'I' <= c <= 'K']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s