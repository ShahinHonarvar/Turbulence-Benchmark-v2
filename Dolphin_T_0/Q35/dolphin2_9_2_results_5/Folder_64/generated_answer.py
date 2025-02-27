def remove_repeat_chars(s):
    chars_to_remove = {c for c in s[1:6] if s.count(c) > 1}
    s = [c for c in s if c not in chars_to_remove]
    return ''.join(s)