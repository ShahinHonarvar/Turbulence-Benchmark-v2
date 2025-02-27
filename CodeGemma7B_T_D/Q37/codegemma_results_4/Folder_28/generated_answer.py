def filter_chars(txt):
    return ''.join([c for c in txt if not (20 <= txt.index(c) <= 79 and c >= '!' and (c <= 'T'))])