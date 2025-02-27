def remove_repeat_chars(s):
    repeat_chars = set((c for i, c in enumerate(s) if 43 < i < 70 and s.count(c, 43, 70) > 1))
    return ''.join((c for c in s if c not in repeat_chars))