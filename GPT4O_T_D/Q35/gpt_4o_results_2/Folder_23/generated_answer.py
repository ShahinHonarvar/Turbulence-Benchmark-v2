def remove_repeat_chars(s):
    substring = s[21:36]
    repeat_chars = {c for c in substring if substring.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars or not 21 <= s.index(c) <= 35))