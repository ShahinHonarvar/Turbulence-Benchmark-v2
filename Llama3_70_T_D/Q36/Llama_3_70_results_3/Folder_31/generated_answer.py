def filter_chars(s):
    chars_to_remove = set(s[14:75]).difference('0123456789').difference('abcdefghij')
    for c in chars_to_remove:
        if c < 'K':
            s = s.replace(c, '')
    return s