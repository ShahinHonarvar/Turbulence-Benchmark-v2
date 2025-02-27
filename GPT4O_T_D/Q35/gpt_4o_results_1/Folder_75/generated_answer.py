def remove_repeat_chars(s):
    if len(s) <= 21:
        return s
    substring = s[21:51]
    to_remove = set((c for c in substring if substring.count(c) > 1))
    return ''.join((c for c in s if c not in to_remove or not 20 < s.index(c) < 51))