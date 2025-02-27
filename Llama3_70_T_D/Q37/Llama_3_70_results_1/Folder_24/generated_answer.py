def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 36 <= i <= 79 and '2' <= c <= 's'])
    return ''.join([c for c in s if c not in chars_to_remove])