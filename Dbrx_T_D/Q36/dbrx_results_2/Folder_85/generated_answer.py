def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 55 or i >= 80 or (not 'S' < c < 's')))