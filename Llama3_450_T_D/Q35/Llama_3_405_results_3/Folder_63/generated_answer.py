def remove_repeat_chars(s):
    chars_to_remove = set((c for c in s[81:86] if s[81:86].count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))