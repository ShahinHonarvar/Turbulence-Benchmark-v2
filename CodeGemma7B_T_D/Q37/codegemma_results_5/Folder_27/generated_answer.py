def filter_chars(s):
    return ''.join([c for c in s if not (range(43, 81) and c >= '=' and (c <= 'E'))])