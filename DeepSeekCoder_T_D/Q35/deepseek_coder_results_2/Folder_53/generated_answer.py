def remove_repeat_chars(s):
    if len(s) < 203:
        return s
    repeat_chars = {c for c in s[200:202] if s[200:202].count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))