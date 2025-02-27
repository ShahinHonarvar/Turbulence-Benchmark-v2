def remove_repeat_chars(s):
    repeat_chars = set((c for i, c in enumerate(s[38:81]) if s[38:81].count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))