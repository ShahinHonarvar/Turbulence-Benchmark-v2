def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    repeat_check = s[45:78]
    repeat_chars = {c for c in repeat_check if repeat_check.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars or s.index(c) < 45 or s.index(c) >= 78))