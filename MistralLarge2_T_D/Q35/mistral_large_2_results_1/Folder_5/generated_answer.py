def remove_repeat_chars(s):
    substring = s[2:8]
    repeated_chars = set((c for c in substring if substring.count(c) > 1))
    return ''.join((c for c in s if c not in repeated_chars))