def filter_chars(s):
    chars_to_filter = set((chr(i) for i in range(46, 86) if '-' <= chr(i) <= 'X'))
    return ''.join((c for c in s if c not in chars_to_filter))