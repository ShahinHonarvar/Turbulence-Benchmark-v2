def filter_chars(s):
    if len(s) < 21:
        return s
    characters_to_remove = {c for c in s[21:44] if '+' <= c <= '8'}
    return ''.join((c for c in s if c not in characters_to_remove))