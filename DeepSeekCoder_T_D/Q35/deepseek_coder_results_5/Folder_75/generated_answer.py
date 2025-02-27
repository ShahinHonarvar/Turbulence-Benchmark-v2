def remove_repeat_chars(s):
    if len(s) < 52:
        return s
    repeat_chars = {c for c in s[20:51] if s[20:51].count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))