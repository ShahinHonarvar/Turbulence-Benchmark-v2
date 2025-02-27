def filter_chars(s):
    if len(s) <= 51:
        return s
    char_set = set((c for c in s[51:92] if 'A' < c < 'Q'))
    return ''.join((c for c in s if c not in char_set))