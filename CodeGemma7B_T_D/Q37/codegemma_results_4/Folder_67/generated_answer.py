def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i >= 19 and i <= 22 and (c not in list(']t'))])