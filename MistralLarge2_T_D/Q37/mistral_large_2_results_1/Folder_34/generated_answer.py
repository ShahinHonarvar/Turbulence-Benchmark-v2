def filter_chars(s):
    to_remove = {c for i, c in enumerate(s) if 54 <= i <= 62 and ')' <= c <= '9'}
    return ''.join((c for c in s if c not in to_remove))