def remove_repeat_chars(s):
    if len(s) < 3:
        return s
    chars_to_remove = {c for c in s[1:2] if s.count(c) > 1}
    return ''.join((c for c in s if c not in chars_to_remove))