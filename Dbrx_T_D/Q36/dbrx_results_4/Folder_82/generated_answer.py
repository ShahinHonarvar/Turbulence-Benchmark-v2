def filter_chars(s):
    filtered = ''.join((c for i, c in enumerate(s) if not (69 < i < 97 and 'V' < c < 'j')))
    return filtered