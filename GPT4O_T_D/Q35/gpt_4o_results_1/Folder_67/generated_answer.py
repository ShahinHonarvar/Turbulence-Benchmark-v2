def remove_repeat_chars(s):
    repeated_chars = set((c for c in s[45:67] if s[45:67].count(c) > 1))
    return ''.join((c for c in s if c not in repeated_chars or not 44 < s.index(c) < 67))