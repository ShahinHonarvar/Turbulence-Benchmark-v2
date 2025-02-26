def filter_chars(s):
    if len(s) < 4:
        return s
    char_to_remove = s[2]
    if '5' <= char_to_remove <= '_':
        return s[:2] + s[3:].replace(char_to_remove, '')
    return s