def filter_chars(s):
    return ''.join([c for c in s if not (42 < ord(c) < 78 and c > '!' and (c < '?'))])