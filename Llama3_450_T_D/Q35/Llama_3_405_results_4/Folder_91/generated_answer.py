def remove_repeat_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s[:6]) if s[:6].count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))