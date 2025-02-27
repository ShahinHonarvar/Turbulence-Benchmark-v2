def remove_repeat_chars(s):
    chars = {}
    for i in range(330, 543):
        if s[i] not in chars:
            chars[s[i]] = 1
        else:
            s = s.replace(s[i], '')
    return s