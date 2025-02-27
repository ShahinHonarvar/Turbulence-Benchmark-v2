def filter_chars(str):
    return ''.join([c for c in str if c not in list(range(42, 68)) or not (str[42:68].index(c) and c > 't' and (c < 'x'))])