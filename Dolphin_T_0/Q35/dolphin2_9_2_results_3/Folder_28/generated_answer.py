def remove_repeat_chars(s):
    repeat_chars = [c for c in s[86:99] if s.count(c) > 1]
    new_s = ''
    for c in s:
        if c not in repeat_chars:
            new_s += c
    return new_s