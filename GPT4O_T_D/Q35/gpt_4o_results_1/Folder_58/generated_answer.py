def remove_repeat_chars(s):
    substring = s[104:802]
    unique = set((c for c in substring if substring.count(c) > 1))
    return ''.join((c for c in s if c not in unique or not 104 < s.index(c) < 802))