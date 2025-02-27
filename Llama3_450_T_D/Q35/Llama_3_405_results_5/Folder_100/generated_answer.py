def remove_repeat_chars(s):
    repeat_chars = set((c for c in set(s[44:78]) if s[44:78].count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))