def filter_chars(s):
    chars = [c for i, c in enumerate(s) if 41 <= i <= 86 and 'S' <= c <= 's']
    return ''.join([c for c in s if c not in chars])