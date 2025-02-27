def filter_chars(s):
    to_remove = [c for i, c in enumerate(s) if 19 <= i <= 92 and '8' <= c <= 'm']
    return ''.join([c for c in s if c not in to_remove])