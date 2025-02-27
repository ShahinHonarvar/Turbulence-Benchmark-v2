def remove_repeat_chars(s):
    part = s[11:28]
    repeat_chars = {c for c in part if part.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars or not 11 < s.index(c) < 28))