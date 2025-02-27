def filter_chars(s):
    if len(s) <= 43:
        return s
    indices_range = s[21:44]
    chars_to_remove = {c for c in indices_range if '+' <= c <= '8'}
    return ''.join((c for c in s if c not in chars_to_remove))