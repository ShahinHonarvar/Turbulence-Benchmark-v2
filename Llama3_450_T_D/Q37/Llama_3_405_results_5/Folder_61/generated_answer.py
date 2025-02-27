def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 5 <= i <= 6 and 'G' <= c <= 'p']
    return ''.join([c for c in s if c not in chars_to_remove])