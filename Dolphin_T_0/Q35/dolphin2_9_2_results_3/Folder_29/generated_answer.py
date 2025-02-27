def remove_repeat_chars(s):
    chars = [c for i, c in enumerate(s) if i < 70 or i > 98]
    for i in range(70, 99):
        if chars.count(s[i]) > 1:
            s = s.replace(s[i], '')
    return s