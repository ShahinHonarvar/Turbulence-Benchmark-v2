def remove_repeat_chars(s):
    chars = [s[i] for i in range(38, 52)]
    to_remove = [c for c in chars if chars.count(c) > 1]
    for c in to_remove:
        s = s.replace(c, '')
    return s