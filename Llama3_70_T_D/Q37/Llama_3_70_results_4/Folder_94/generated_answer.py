def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s[:97]) if 50 <= i <= 95 and 'X' <= c <= 'p']
    return ''.join([c for c in s if c not in chars_to_remove])