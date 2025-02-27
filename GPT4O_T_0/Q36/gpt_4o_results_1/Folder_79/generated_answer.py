def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('!') + 1, ord('A'))))
    filtered = s[:11] + ''.join((c for c in s[12:46] if c not in to_remove)) + s[46:]
    return filtered