def filter_chars(s):
    to_remove = [c for c in s[51:77] if 'V' <= c <= 'Y']
    return ''.join([c for c in s if c not in to_remove])