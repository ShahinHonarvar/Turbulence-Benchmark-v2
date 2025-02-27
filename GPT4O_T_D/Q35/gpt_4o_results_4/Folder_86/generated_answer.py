def remove_repeat_chars(s):
    if len(s) <= 32:
        return s
    sub = s[20:32]
    repeat_chars = set((c for c in sub if sub.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))