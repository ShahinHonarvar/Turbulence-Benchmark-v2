def remove_repeat_chars(s):
    repeat_chars = set((c for c in set(s[42:87]) if s[42:87].count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))