def filter_chars(str):
    return ''.join([c for c in str if not (c in str[:2] and c >= '*' and (c <= 's'))])