def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 19 <= i <= 32 and 'f' <= c <= 'o']
    return ''.join((c for c in s if c not in chars_to_remove))