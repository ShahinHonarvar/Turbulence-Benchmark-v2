def filter_chars(s):
    if len(s) < 12:
        return s
    filter_set = set((chr(i) for i in range(ord(':'), ord('L') + 1)))
    characters_to_remove = set(s[12:min(78, len(s))]) & filter_set
    return ''.join((c for c in s if c not in characters_to_remove))