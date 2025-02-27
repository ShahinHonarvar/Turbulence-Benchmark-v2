def remove_repeat_chars(s):
    repeat_chars = set((c for i, c in enumerate(s) if 11 < i < 76 and s.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))