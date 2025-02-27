def remove_repeat_chars(s):
    target_chars = s[1:2]
    repeat_chars = {c for c in target_chars if s.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))