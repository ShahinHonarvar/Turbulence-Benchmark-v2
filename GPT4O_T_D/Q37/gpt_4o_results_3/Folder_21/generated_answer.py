def filter_chars(s):
    characters_to_remove = set((c for c in s[603:760] if 'Q' <= c <= 'h'))
    return ''.join((c for c in s if c not in characters_to_remove))