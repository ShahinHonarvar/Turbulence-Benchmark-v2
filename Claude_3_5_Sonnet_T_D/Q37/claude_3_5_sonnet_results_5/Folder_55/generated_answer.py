def filter_chars(s):
    characters_to_remove = set((c for i, c in enumerate(s) if 1 <= i <= 5 and '$' <= c <= ';'))
    return ''.join((c for c in s if c not in characters_to_remove))