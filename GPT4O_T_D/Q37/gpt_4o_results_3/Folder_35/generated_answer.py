def filter_chars(s):
    to_remove = set(s[155:404]) & set((chr(i) for i in range(ord('('), ord(']') + 1)))
    return ''.join((c for c in s if c not in to_remove))