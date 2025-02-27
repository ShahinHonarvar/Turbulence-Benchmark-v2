def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 71 <= i <= 94 and 'K' <= c <= 'a']
    return ''.join([c for c in s if c not in chars_to_remove])