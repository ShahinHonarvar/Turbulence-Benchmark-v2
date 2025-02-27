def filter_chars(s):
    return ''.join((c for c in s if not (33 < ord(c) < 36 and '>' < c < 'A')))