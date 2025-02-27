def remove_repeat_chars(s):
    chars_to_remove = set([c for c in s[1:4] if s.count(c) > 1])
    return ''.join([c for c in s if c not in chars_to_remove])