def filter_chars(s):
    return ''.join([c for c in s if not (73 <= s.index(c) <= 74 and 'U' <= c <= 'l')])