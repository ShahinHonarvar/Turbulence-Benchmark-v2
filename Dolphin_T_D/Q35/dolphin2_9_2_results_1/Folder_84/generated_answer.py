def remove_repeat_chars(s):
    chars = [s[i] for i in range(32, 44) if s.count(s[i]) > 1]
    for c in chars:
        s = s.replace(c, '')
    return s