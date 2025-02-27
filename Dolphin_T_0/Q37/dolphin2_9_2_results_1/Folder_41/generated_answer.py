def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 26 or i > 64 or (not 'V' <= c <= 'o')))