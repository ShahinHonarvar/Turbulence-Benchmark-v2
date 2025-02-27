def filter_chars(txt):
    return ''.join([c for c in txt if ord(c) <= 26 or ord(c) >= 76 or (not 'A' <= c < 'i')])