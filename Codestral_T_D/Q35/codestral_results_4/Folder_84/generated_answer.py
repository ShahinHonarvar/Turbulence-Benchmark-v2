def remove_repeat_chars(s):
    chars = s[32:44]
    repeat_chars = [c for c in chars if chars.count(c) > 1]
    for c in repeat_chars:
        s = s.replace(c, '')
    return s