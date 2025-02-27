def remove_repeat_chars(s):
    chars = set()
    for i in range(19, 32):
        if s[i] in chars:
            s = s.replace(s[i], '')
        else:
            chars.add(s[i])
    return s