def filter_chars(str):
    return ''.join([c for c in str if not (20 <= ord(c) <= 62 and 'i' <= c <= 'k')])