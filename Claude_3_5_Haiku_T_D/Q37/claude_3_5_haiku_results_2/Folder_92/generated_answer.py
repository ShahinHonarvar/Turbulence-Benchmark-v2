def filter_chars(s):
    if len(s) < 5:
        return s
    char_to_remove = s[4]
    if '7' <= char_to_remove <= 'o':
        return ''.join((c for c in s if c != char_to_remove))
    return s