def remove_repeat_chars(s):
    chars_to_remove = [c for c in s[50:200] if s[50:200].count(c) > 1]
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s