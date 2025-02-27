def remove_repeat_chars(s):
    if len(s) < 65:
        return s
    repeat_chars = {c for c in s[35:64] if s[35:64].count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))