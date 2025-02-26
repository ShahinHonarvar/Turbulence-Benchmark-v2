def remove_repeat_chars(s):
    repeat_chars = set((c for c in s[3:5] if s[3:5].count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))