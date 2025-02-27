def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (38 <= i <= 54 and ':' <= c <= 'r')))