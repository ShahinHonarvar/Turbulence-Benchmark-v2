def remove_repeat_chars(s):
    chars_to_remove = set((c for c in set(s[10:80]) if s[10:80].count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))