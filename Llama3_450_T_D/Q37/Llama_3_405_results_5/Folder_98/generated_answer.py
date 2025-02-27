def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 8 <= i <= 9 and 'R' <= c <= 't']
    return ''.join([c for c in s if c not in chars_to_remove])