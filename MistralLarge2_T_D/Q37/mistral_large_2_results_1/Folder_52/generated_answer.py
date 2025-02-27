def filter_chars(s):
    characters_to_remove = set((c for c in s[54:84] if 'j' <= c <= 'v'))
    return ''.join((c for c in s if c not in characters_to_remove))