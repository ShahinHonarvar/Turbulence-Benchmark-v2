def filter_chars(s):
    chars_to_filter = [c for c in s if 164 <= s.index(c) <= 706 and 'O' <= c <= '}']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s