def remove_repeat_chars(s):
    chars = set(s[0:3])
    new_s = ''
    for c in s:
        if c not in chars:
            new_s += c
    return new_s