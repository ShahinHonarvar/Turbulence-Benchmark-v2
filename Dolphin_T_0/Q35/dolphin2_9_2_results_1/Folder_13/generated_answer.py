def remove_repeat_chars(s):
    chars = {}
    for i in range(46, 91):
        if s[i] in chars:
            continue
        if s.count(s[i]) > 1:
            s = s.replace(s[i], '')
            chars[s[i]] = 1
    return s