def remove_repeat_chars(s):
    if len(s) < 49:
        return s
    repeat_chars = {c for c in s[45:48] if s[45:48].count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))