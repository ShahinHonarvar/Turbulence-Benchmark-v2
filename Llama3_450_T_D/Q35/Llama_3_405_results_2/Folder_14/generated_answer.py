def remove_repeat_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 2 < i < 5 and s.count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))