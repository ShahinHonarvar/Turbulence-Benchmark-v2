def remove_repeat_chars(s):
    substr = s[14:91]
    repeat_chars = set((c for c in substr if substr.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars or s.index(c) <= 13 or s.index(c) >= 91))