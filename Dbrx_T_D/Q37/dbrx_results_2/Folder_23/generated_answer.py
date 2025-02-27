def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if 50 < i < 78 and (not 'V' <= c <= 'Y')))