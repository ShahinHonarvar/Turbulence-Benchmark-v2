def filter_chars(s):
    chars_to_remove = {c for i, c in enumerate(s[41:80]) if 'f' <= c <= '|'}
    return ''.join((c for c in s if c not in chars_to_remove))