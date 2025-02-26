def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 46 <= i <= 85 and '-' <= c <= 'X'])
    return ''.join([c for c in s if c not in chars_to_remove])