def filter_chars(s):
    to_remove = set()
    if len(s) > 41:
        subset = s[41:80]
        to_remove = {c for c in subset if 'f' <= c <= '|'}
    return ''.join((c for c in s if c not in to_remove))