def filter_chars(s):
    to_remove = [c for c in s[71:97] if '_' <= c <= 'o']
    return ''.join([c for c in s if c not in to_remove])