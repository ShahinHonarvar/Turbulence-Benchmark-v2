def remove_repeat_chars(s):
    if len(s) < 93:
        return s
    chars_to_remove = set((c for c in set(s[72:93]) if s[72:93].count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))