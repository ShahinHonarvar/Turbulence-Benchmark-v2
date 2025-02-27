def remove_repeat_chars(s):
    if len(s) < 10:
        return s
    repeat_chars = {c for c in s[1:9] if s[1:9].count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))