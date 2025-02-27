def filter_chars(s):
    to_remove = [c for c in s[521:723] if c >= '>' and c <= '_']
    return ''.join([c for c in s if c not in to_remove])