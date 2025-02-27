def remove_repeat_chars(s):
    repeat_chars = set((c for c in s[200:202] if s[200:202].count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))