def remove_repeat_chars(s):
    substring = s[74:84]
    repeating_chars = set((c for c in substring if substring.count(c) > 1))
    return ''.join((c for c in s if c not in repeating_chars or c not in substring))