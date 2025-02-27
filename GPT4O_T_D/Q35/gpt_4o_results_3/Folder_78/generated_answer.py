def remove_repeat_chars(s):
    substring = s[63:96]
    repeat_chars = set((c for c in substring if substring.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars or s.index(c) > 95 or s.index(c) < 63))