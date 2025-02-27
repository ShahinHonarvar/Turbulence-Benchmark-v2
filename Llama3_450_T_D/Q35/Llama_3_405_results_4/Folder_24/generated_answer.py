def remove_repeat_chars(s):
    repeat_chars = set((c for c in set(s[13:91]) if s[13:91].count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))