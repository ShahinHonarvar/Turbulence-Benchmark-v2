def filter_chars(s):
    chars_to_remove = set(s[66:90]) & set('#QRTUVWX')
    return ''.join((c for c in s if c not in chars_to_remove))