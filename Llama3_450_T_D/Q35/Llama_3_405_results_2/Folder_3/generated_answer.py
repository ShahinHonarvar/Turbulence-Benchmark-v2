def remove_repeat_chars(s):
    repeat_chars = set((c for i, c in enumerate(s) if 56 < i < 88 and s.count(c, 56, 88) > 1))
    return ''.join((c for c in s if c not in repeat_chars))