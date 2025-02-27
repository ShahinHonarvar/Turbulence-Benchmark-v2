def filter_chars(s):
    to_remove = [c for c in s[36:57] if c.isdigit() and '6' <= c <= '_']
    return ''.join([c for c in s if c not in to_remove])