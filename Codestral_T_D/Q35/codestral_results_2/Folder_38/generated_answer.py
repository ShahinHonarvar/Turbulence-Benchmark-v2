def remove_repeat_chars(s):
    chars = {}
    for i in range(36, 85):
        c = s[i]
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for c, count in chars.items():
        if count > 1:
            s = s.replace(c, '')
    return s