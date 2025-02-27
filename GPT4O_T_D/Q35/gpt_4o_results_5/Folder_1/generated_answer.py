def remove_repeat_chars(s):
    part = s[18:88]
    repeated_chars = {c for c in part if part.count(c) > 1}
    return ''.join((c for c in s if c not in repeated_chars or not 18 <= s.index(c) < 88))