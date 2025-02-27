def filter_chars(s):
    to_remove = {c for c in s[41:80] if 'f' <= c <= '|'}
    return ''.join((c for c in s if c not in to_remove))