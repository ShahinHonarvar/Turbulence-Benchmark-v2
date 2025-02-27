def filter_chars(s):
    to_remove = [c for c in s[521:722] if c >= '>' and c <= '_']
    s = ''.join([c for c in s if c not in to_remove])
    return s