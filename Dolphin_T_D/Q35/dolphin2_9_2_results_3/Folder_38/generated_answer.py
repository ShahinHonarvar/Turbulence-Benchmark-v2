def remove_repeat_chars(s):
    chars_to_remove = {c for c in s[36:86] if s.count(c) > 1}
    new_s = ''
    for c in s:
        if c not in chars_to_remove:
            new_s += c
    return new_s