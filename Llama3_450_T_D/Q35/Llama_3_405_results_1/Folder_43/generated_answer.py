def remove_repeat_chars(s):
    repeat_chars = set((c for c in set(s[10:28]) if s[10:28].count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))