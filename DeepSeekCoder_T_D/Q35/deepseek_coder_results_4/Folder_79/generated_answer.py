def remove_repeat_chars(s):
    repeat_chars = {c for i, c in enumerate(s) if 1 < i < 8 and s.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))