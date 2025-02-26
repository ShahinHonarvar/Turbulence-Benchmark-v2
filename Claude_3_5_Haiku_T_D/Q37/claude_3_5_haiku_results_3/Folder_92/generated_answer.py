def filter_chars(s):
    if len(s) <= 4:
        return s
    char_to_remove = s[4]
    if '7' <= char_to_remove <= 'o':
        return s.replace(char_to_remove, '')
    return s