def remove_repeat_chars(s):
    chars = [s[i] for i in range(49, 74)]
    for c in chars:
        if chars.count(c) > 1:
            s = s.replace(c, '')
    return s