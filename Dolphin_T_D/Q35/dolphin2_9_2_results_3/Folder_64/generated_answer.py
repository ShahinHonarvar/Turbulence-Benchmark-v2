def remove_repeat_chars(s):
    chars_to_remove = {c for c, _ in s.count(c) if c not in s[0:5] and s.count(c) > 1}
    return ''.join([c for c in s if c not in chars_to_remove])