def filter_chars(s):
    if len(s) < 10:
        return s
    char_to_remove = s[8]
    if 'R' <= char_to_remove <= 't':
        return s.replace(char_to_remove, '')
    return s