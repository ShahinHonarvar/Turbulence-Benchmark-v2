def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(46, 91) if 'D' < chr(i) < 'H'))
    return ''.join((c for c in s if c not in chars_to_remove))