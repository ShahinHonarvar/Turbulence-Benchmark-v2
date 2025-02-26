def remove_repeat_chars(s):
    repeat_chars = set((c for c in s[46:48] if s[46:48].count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))