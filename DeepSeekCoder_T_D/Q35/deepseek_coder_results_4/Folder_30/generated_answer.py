def remove_repeat_chars(s):
    target_range = s[22:24]
    repeat_chars = {c for c in target_range if s.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))