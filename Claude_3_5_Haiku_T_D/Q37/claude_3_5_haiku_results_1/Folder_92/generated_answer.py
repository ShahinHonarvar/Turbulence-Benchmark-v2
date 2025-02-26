def filter_chars(s):
    if len(s) < 5:
        return s
    char_at_index_4 = s[4]
    if '7' <= char_at_index_4 <= 'o':
        return s.replace(char_at_index_4, '')
    return s