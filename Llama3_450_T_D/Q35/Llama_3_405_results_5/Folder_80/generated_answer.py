def remove_repeat_chars(s):
    repeat_chars = set((c for i, c in enumerate(s[57:84]) if s[57:84].count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))