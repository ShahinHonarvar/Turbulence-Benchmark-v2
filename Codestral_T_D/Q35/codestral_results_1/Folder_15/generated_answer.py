def remove_repeat_chars(s):
    to_remove = set((c for c in s[1:5] if s.count(c) > 1))
    return ''.join((c for c in s if c not in to_remove))