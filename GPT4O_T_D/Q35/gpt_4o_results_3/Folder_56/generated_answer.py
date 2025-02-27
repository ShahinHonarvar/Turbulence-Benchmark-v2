def remove_repeat_chars(s):
    if len(s) <= 9:
        return s
    substring = s[8:9]
    repeat_chars = set((c for c in substring if substring.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))