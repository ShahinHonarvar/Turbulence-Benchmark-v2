def filter_chars(s):
    characters_to_remove = set((c for c in s[2:7] if '-' < c < 'L'))
    return ''.join((c for c in s if c not in characters_to_remove))