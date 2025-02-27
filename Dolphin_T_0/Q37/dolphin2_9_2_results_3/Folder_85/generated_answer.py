def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (28 <= i <= 65 and c >= 'O' and (c <= 'd'))])