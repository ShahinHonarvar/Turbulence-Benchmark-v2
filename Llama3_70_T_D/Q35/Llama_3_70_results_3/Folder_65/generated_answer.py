def remove_repeat_chars(s):
    repeat_chars = set((c for c in s[51:76] if s[51:76].count(c) > 1))
    return ''.join((c for i, c in enumerate(s) if c not in repeat_chars))