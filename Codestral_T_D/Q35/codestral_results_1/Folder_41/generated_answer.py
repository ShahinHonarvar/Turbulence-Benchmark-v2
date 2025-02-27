def remove_repeat_chars(s):
    chars = set(s[3:8])
    return ''.join((c for c in s if c not in chars or s[3:8].count(c) == 1))