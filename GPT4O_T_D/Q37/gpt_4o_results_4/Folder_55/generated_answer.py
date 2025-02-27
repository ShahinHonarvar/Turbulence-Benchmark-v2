def filter_chars(s):
    if len(s) <= 1:
        return s
    characters_to_remove = {c for c in s[1:6] if '$' <= c <= ';'}
    return ''.join((c for c in s if c not in characters_to_remove))